#! /usr/bin/python3
# -*- coding:utf-8 -*-
import psycopg2
import argparse
import time
import random 
parser = argparse.ArgumentParser()
parser.add_argument('-n',help="Study number")
parser.add_argument('-H',help="set needed hours")
parser.add_argument('-t',help="set times")
parsers = parser.parse_args()
try:
    conn = psycopg2.connect(database="tmplate1",user="postgres",password="postgres",host="192.168.10.13",port="5432")
    cur = conn.sursor()
    print("[+] PG Connected !")
except:
    print("[-] Connection Error ")
    exit()
alreadyDone = 0             #已经更新的时间
dates = []                  #日期列表
dateCount = 0               #三天内的记录数目
resultId = ''


def execute(number,hours,time):
    seconds = hours*3600
    global resultId
    global dates
    try:
        cur = execute('select id,first_name from "public"."jcms_system_user" where username=%s;'%number)
        row = cur.fetchall()
        resultId = row[0][0]        #找出用户id
        print("++++++++  username is %s  ++++++++"%(row[0][1]))
        cur = execute('select time,datetime,textid from "public"."user_study_history" where userid=%s'%resultId)
        row = cur.fetchall()
        for x in len(row):      #选出所有的日期，然后集中
            dates[x] = row[x][1]
            print("*** time:  %s, datetime: %s, textid:  %s"%(row[x][0],row[x][1],row[x][2]))
        #nowTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        timeFileter()               #含全局变量函数里不能传此全局变量(dates)
        while(alreadyDone < seconds & dateCount != 0):
            update(seconds)
        else:
            print('[+] Almost Done')
            conn.close()
            exit()

    except:
        print("[-] Select Error!")
        conn.close()
        exit()
    #updateResult = update(seconds)
    #while(updateResult < hours*60):
     #   updateHours(dates)

def update(seconds):
    if(type(dates) == list):
        randomResult = Random(seconds,dates)
        global alreadyDone
        try:
            cur = conn.execute('update "public"."user_study_history" set time=%s,datetime=%s where where userid=%s'%(randomResult[0],randomResult[1],resultId))
            print('[+] Update success')
        except:
            print("[-] Update Error")
            conn.close()
            exit()
        alreadyDone += randomResult[0]
    else:
        print('[-] wrong date format')
        conn.close()
        exit()
    return alreadyDone


def Random(seconds):
    global dateCount
    global dates
    randomSecond = int(random.uniform(3600,12000))          #生成随机秒数
    randomHours = range(8,18)                               #限制在线时间在8-18小时范围内
    for x in range(len(dates)).reverse():
        tmpDate = time.mktime(strptime(dates[x],"%Y-%m-%d %H:%M:%S")) - randomSecond        #转换为float时间格式，并减去刚生成的随机秒数
        tmpDateH = int(time.strftime('%H',time.localtime(tmpDate)))
        tmpDate_d = int(time.strftime('%d',time.localtime(tmpDate)))
        tmpDate_m = int(time.strftime('%m',time.localtime(tmpDate)))
        dates[x] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(tmpDate))           #转换为年月日……的时间格式，准备修改数据 >>>
        if(tmpDateH < 8):
            dates[x] = dates[x][:11] + '08' + dates[x][13:]
        elif(tmpDateH > 18):
            dates[x] = dates[x][:11] + '18' + dates[x][13:]

    dateCount -= 1
    
    return [randomSecond,randomDate]        #返回随机秒数和随机日期


def timeFileter():
    global dates
    global dateCount
    #dateFormatChange = []
    lastDay = dates[-1].split('-')[2].split(' ')[0]         #获取最后一天的值
    #lastHour = dates[-1].split(' ')[1].split(':')[0]
    for x in len(dates):
        tmp = dates[x].split('-')[2].split(' ')[0]
        if(tmp+3 < lastDay):                        #去除三天前的数据
            dates.pop(x)
            x -= 1
    dateCount = len(dates)
    #for x in len(dates):
     #   tmp = time.mktime(time.strptime(dates[x],"%Y-%m-%d %H:%M:%S"))
      #  dateFormatChange[x] = time.strftime("%m-%d-%H-%M",time.localtime(tmp)       #转化为 月-日-小时-分钟 格式
    #for y in len(dates):
     #   if(int(dates[y].split('-')[2].split(' ')[0])-3 < 0):               #判断三天前是否为上个月
      #      dateSplit[0] = int(dateSplit[0]) - 1
       # else:
        #    exit()


if __name__ == '__main__':
    try:
        execute(parsers.n,parsers.H,parsers.t)
    except:
        print('[-] please give me three parameter')
