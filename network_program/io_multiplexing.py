#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import fcntl
import socket
import select

response = 'HTTP/1.1 200 OK\r\nConnection: Close\r\nContent-Length: 1\r\n\r\nA'

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
server.listen(32)

flags = fcntl.fcntl(server.fileno(), fcntl.F_GETFL)
fcntl.fcntl(server.fileno(), fcntl.F_SETFL, flags | os.O_NONBLOCK)

clients = set([])

while True:
    rlist = clients.copy()
    rlist.add(server)

    rlist, wlist, xlist = select.select(rlist, [], [], 10)

    for fd in rlist:
        if fd == server:
            client, clientaddr = server.accept()
            clients.add(client)
        else:
            request = fd.recv(4096)
            fd.send(response)
            clients.remove(fd)
            fd.close()
