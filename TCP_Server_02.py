import traceback

__author__ = 'chenwei'


import socketserver

count = 0;


class MyStreamRequestHandlerr(socketserver.StreamRequestHandler):
    """
    #继承StreamRequestHandler，并重写handle方法
    #（StreamRequestHandler继承自BaseRequestHandler）
    """
    def handle(self):

        print('handle()',self.client_address)
        data = self.rfile.readline().strip()
        print(data)
        self.wfile.write('xxx'.encode())


if __name__ == "__main__":
    HOST, PORT = "localhost", 10001

    server = socketserver.TCPServer((HOST, PORT), MyStreamRequestHandlerr)
    server.serve_forever()