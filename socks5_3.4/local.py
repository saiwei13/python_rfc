__author__ = 'chenwei'

import sys
import socketserver
import struct
import socket
import select
import simplejson
import time

PORT = 1081

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class Hosts():
    def __init__(self, hosts=None):
        self.hosts = hosts
        self.index = 0
    def get_host(self):
        if len(self.hosts) == 0:
            print('Sorry, you have no sock5 server alive now')
            return None
        return self.hosts[0]

hosts = Hosts()

class Sock5Local(socketserver.StreamRequestHandler):
    def handle(self):
        print ('[%s] socks connection from %s' % (time.ctime(), self.client_address))
        sock = self.connection
        try:
            addr = hosts.get_host()
            if not addr:
                return

            remote = socket.create_connection(addr)
            print ("[%s] connection to %s" % (time.ctime() ,addr[0]))
        except:
            #hosts.hosts.remove(addr)
            print ('Socket error')
            return
        self.handle_chat(sock, remote)

    def handle_chat(self, sock, remote):
        fdset = [sock, remote]
        try:
            while True:
                r,w,e = select.select(fdset, [], [])
                if sock in r:
                    if self.send(remote, self.recv(sock, 2096)) <= 0:
                        break
                if remote in r:
                    if self.send(sock, self.recv(remote, 2096)) <= 0:
                        break
        except:
            pass
        finally:
            remote.close()
            sock.close()

    def send(self, sock, data):
        return sock.send(data)

    def recv(self, sock, l):
        return sock.recv(l)

def main():
    hosts_str = open('cfg.json','r').read()
    try:
        hosts_ = simplejson.loads(hosts_str)['hosts']
    except simplejson.decoder.JSONDecodeError:
        print ('Json format error')
        return

    if not hosts_:
        print ('file cfg.json is empty')
        return
    hosts.hosts = hosts_

    print(hosts.hosts)
    print(hosts.get_host())

    server = ThreadingTCPServer(('', PORT), Sock5Local)
    server.allow_reuse_address = True
    print ('start local proxy at port {0}'.format(PORT))
    server.serve_forever()

if __name__ == '__main__':
    main()