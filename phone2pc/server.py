#!/usr/bin/python3
# coding=utf-8

import socket
import queue
import threading

class SubClient(threading.Thread):
    def __init__(selfq,q):
        super(SubClient, self).__init__()
        self.q = q

    def run():
        pass


def pull(conn):
    data = conn.recv(2048).decode()
    if data == 'q':
        conn.close()
    else:
        print(data)
    return data

def push(conn):
    while 1:
        string = input('input sth: ').strip().encode()
        conn.send(string)
        #for x in client_list:
        #    x.send(string)

def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 6666))
    return s

q = queue.Queue()
if __name__ == '__main__':
    server = start()
    server.listen(10)
    client_list = []
    while 1:
        conn, addr = server.accept()
        client_list.append(conn)
        print(addr,'  connected !')
        tc = threading.Thread(target=push, args=(conn,))
        ts = threading.Thread(target=pull, args=(conn,))
        tc.start()
        ts.start()
