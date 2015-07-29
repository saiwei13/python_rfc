__author__ = 'chenwei'


import socket


def test():
    address = ('0.0.0.0', 10001)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # s = socket.socket()
    s.bind(address)
    s.listen(5)

    while True:
        ss, addr = s.accept()
        print ('got connected from',addr)
        msg = 'byebye'
        ss.send(msg.encode())
        ra = ss.recv(512)
        print (ra)
        ss.close()
    s.close()


if __name__ == '__main__':
    test()