#! /usr/bin/python
#coding:utf-8
from bs4 import BeautifulSoup
from qqbot import QQBot
import requests,sys,MySQLdb,re
reload(sys)
sys.setdefaultencoding('utf-8')     #重载系统编码
chatList = []   #聊天列表
i = 1
sensitive = []  #敏感词列表
try:        #数据库连接
    conn = MySQLdb.connect(host='localhost',port=3306,user='',passwd='',db='qq',charset='utf8')
    cur = conn.cursor()
    #取出聊天名单
    cur.execute('select name from chatList')
    chat = cur.fetchall() #此处为二元元组
    for x in chat:
        chatList.append(x[0])      #变为一元列表
        i = i + 1
    #取出敏感字符
    cur.execute('select Text from sensitiveText')
    sen = cur.fetchall()    #同上为二元元组
    for x in sen:
        sensitive.append(x[0])

except MySQLdb.Error,e:
    print (e)

#百科功能
def search(key):
    url = 'http://baike.baidu.com/item/%s'%key
    startSearch = requests.get(url)
    result = startSearch.text
    result1 = re.findall(r'</div><div class="lemma-summary" label-module="lemmaSummary">\n<div class="para" label-module="para">(.*?)</div>\n</div>',result)
    regex = re.compile(r'<(S*?)[^>]*>.*?|<.*? />')
    result2 = result1[0].decode('utf-8','ignore')
    print(type(result2))
    result3 = re.sub(regex,'',result2)
    #result = BeautifulSoup(startSearch.text)
    #result1 = result.find_all('div','lemma-summary')
    #result2 = re.findall(r'label-module="para">(.*?)</div>\n</div>',result1[0])
    #result3 = result2[0].replace(re.findall(r'<(S*?)[^>]*>.*?|<.*? /> ',resule2[0]),'')
    return result3

myqq = QQBot()
@myqq.On('qqmessage')
def handler(bot,message):
    if unicode(message.contact.name,'utf-8') in chatList:       #妈的，非得转码一下才行，要是3.x的话就不需要转码了😭
        #敏感字符检测
        for x in sensitive:
            if message.content.find(x) >= 0:
                bot.SendTo(message.contact,'楼上包含敏感字符，并回复楼上 草泥马')
                return
        #检测搜索关键字
        if '搜索' in message.content:
            bot.SendTo(message.contact,search(message.content.split('搜索')[1]))
            return
  #发送数据库里对应的回答
        if message.content.find('@Rootkit') >= 0:
            bot.SendTo(message.contact,'叫我主人干嘛😊')
            return
        try:
            sql = 'select answer from record where question="%s"'%message.content
            an = cur.execute(sql)
            if an > 0:
                msg = cur.fetchone()
                bot.SendTo(message.contact,msg[0])
                    #return
            else:
                bot.SendTo(message.contact,'抱歉，数据库里没有这句话')
                    #return
        except MySQLdb.Error,ex:
                print(ex)
myqq.Login()
myqq.Run()

