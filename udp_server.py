__author__ = 'chenwei'


import socket
import sys
#创建UDP套接字



TAG = 'SERVER: '

# ip = '10.61.128.26'
ip = '106.186.118.123'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#绑定套接字端口号
server_address = (ip, 10000)
print(TAG,'starting up on %s port %s' % server_address)
sock.bind(server_address)

while True:
    print(TAG, '\nwaiting to receive message')
    #使用recvfrom()从套接字读取消息、并返回数据、还会返回发出此消息的客户端地址
    data, address = sock.recvfrom(4096)

    print(TAG, 'received %s bytes from %s' %(len(data), address))
    print(TAG, data)

    if data:
        #蒋收到的数据通过sendto()发送到指定地址
        sent = sock.sendto(data, address)
        print(TAG, 'sent %s bytes back to %s' %(sent, address))