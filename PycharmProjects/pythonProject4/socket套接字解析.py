#coding=utf-8
#创建TCP服务器
import socket
import time
from time import ctime

HOST = '127.0.0.1'
PORT = 8080
BUFSIZE=1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)
addr=(HOST,PORT)
while True:
    print('waiting for connection...')
    sock,addr =sock.accept()
    print('...connected from:',addr)
    while True:
        data =sock.recv(BUFSIZE).decode()
        print('date=',data)
        if not data:
            break
        sock.send(('[%s] %s' %(ctime(),data)).encode())
sock.close()



#coding=utf-8
#创建TCP客户端

import socket

HOST = '127.0.0.1'
PORT = 8080
BUFSIZE = 1024
ADDR=(HOST,PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
    data = input('> ')
    if not data:
        break
    sock.send(data.encode())
    data = sock.recv(BUFSIZE).decode()
    if not data:
        break
    print(data)

sock.close()
