__author__ = 'chenwei'


import socket

ip = '127.0.0.1'

def test():
    address = (ip, 10001)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(address)

    msg = 'hihi2'
    s.send(msg.encode())


    data = s.recv(512)
    print('the data received is',data)

    s.close()

if __name__ == '__main__':
    test()