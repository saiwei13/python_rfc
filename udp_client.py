__author__ = 'chenwei'

TAG = "CLIENT : "

import socket
import sys

ip = '106.186.118.123'

#创建UDP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (ip, 10000)
# message = "This is the message.
# It will be repeated."
message = "abcd"

try:
    #发送数据
    print(TAG, 'sending "%s"' % message)
    sent = sock.sendto(message.encode(), server_address)
    #sendto()将数据发送到指定地址

    print(TAG, 'waiting to receive')
    data, server = sock.recvfrom(4096)
    print(TAG, 'received "%s"' % data)

finally:
    print(TAG, 'closing socket')
    sock.close()
