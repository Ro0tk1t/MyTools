#! /usr/bin/python3
#encoding:utf-8

import time
import json
import requests
import argparse
pars = argparse.ArgumentParser()
pars.add_argument('-s',help='要刷的总步数')
parser = pars.parse_args()

body = {'access_token':'****************','openid':'******************','steps':''}
blen = len(body)
head = {'Content-Length':'97',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host':'cloud-vip.bmob.cn',
        'Connection':'close',
        'User-Agent':"Apache-HttpClient/UNAVAILABLE (java 1.4)"}
def timely(init,body,head):
    body['steps']= str(init)
    t = time.strftime('%H:%M:%S',time.localtime())
    each = requests.post('http://cloud-vip.bmob.cn/af8bdb392f7eceff/qqyundong',data=body,headers=head)
    init += 800
    print('[+] '+ t + '  已刷：%s'%init + ' 步')
    time.sleep(40)
    return timely(init,body,head)

if parser.s:
    body['steps'] = parser.s
    a = requests.post('http://cloud-vip.bmob.cn/af8bdb392f7eceff/qqyundong',data=body,headers=head)
    print(body)
    print(a.text)

else:
    timely(10000,body,head)
