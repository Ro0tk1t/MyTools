#!/usr/bin/python3
# coding=utf-8

import threading
import socket
import nmap
import os,re

def get_local_ip():
    tmp = os.popen("ifconfig | grep inet | grep -v 127.0.0.1 | awk '{print $2}'").read().strip().split('\n')
    ips = []
    for x in tmp:
        try:
            y = re.search(r'[1-9][0-9]{0,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',x).group()
            ips.append(y)
        except AttributeError:
            continue
    return ips if len(ips) > 1 else ips[0]

def scan(aimed, cond):
    cond.acquire()
    n = nmap.PortScanner()
    print('[*] scan for host  %s' % aimed)
    result = n.scan(aimed, str(port))
    if result['scan'] and result['scan'].get(aimed).get('tcp').get(port).get('state') == 'open':
        print('\n[+] found host {}\n'.format(aimed))
        globals()['scan_result'].append(aimed)
        cond.notify()
    cond.release()
    return 0

def connect(cond):
    cond.acquire()
    print('[*] wait for connect...')
    cond.wait()
    s = socket.socket()
    s.connect((scan_result[0], port))
    print('[+] connect to server')
    cond.release()
    while 1:
        try:
            data = s.recv(2048).decode('utf-8')
            print('server message: %s' % data)
        except:
            print('error recave message !')

def main():
    ips = get_local_ip()
    if isinstance(ips, list):
        ip = ips[0]
    else:
        ip = ips

    dot = ip.rindex('.')
    net_addr = ip[:dot]
    ts = threading.Thread(target=connect, args=(cond,))
    ts.start()
    for x in range(2, 255):
        aimed = net_addr +'.'+ str(x)
        t = threading.Thread(target=scan, args=(aimed,cond))
        t.start()
        #t.join()

if __name__ == '__main__':
    scan_result = []
    port = 6666
    cond = threading.Condition()
    semaphore = threading.Semaphore(3)
    main()
