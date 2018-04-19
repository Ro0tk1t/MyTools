#!/usr/bin/python3
# coding=utf-8

import threading
import socket
from sys import argv

def recive(conn):
    while 1:
        data = conn.recv(2048).decode()
        print(data)

if __name__ == '__main__':
    s = socket.socket()
    s.connect((argv[1], int(argv[2])))
    t = threading.Thread(target=recive, args=(s,))
    t.start()
    while 1:
        string = input('send: ').strip().encode()
        s.send(string)

