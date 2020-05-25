# -*- coding: utf-8 -*-
import socket

print('============================================')
print('exit - отключается от сервера (обязательно перед выходом!)')
print('============================================')

HOST = 'localhost'
PORT = 9990

print('\nВведите логин:')
lgd = False
pswd = False

while True:
    request = input('>')

    sock = socket.socket()
    sock.connect((HOST, PORT))

    if not lgd:
        name = request
        request = '<Login is:> ' + request
        sock.send(request.encode())
        lgd = True

    else:
        sock.send(request.encode())

    try:
        response = sock.recv(1024).decode()
    except:
        pass

    print(response)

    sock.close()

    if request == "exit":
        print('Сеанс завершен')
        break