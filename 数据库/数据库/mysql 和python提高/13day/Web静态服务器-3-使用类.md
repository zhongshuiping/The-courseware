## Web静态服务器-3-使用类


```python
#coding=utf-8
import socket
import re


class WSGIServer(object):

    def __init__(self, server_address):
        # 创建一个tcp套接字
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 允许立即使用上次绑定的port
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定
        self.listen_socket.bind(server_address)
        # 变为被动，并制定队列的长度
        self.listen_socket.listen(128)

    def serve_forever(self):
        "循环运行web服务器，等待客户端的链接并为客户端服务"
        while True:
            # 等待新客户端到来
            self.client_socket, client_address = self.listen_socket.accept()
            self.handleRequest()

    def handleRequest(self):
        "为一个客户端进行服务"
        recv_data = self.client_socket.recv(1024).decode('utf-8')
        requestHeaderLines = recv_data.splitlines()
        for line in requestHeaderLines:
            print(line)

        request_line = requestHeaderLines[0]
        get_file_name = re.match("[^/]+(/[^ ]*)", request_line).group(1)
        print("file name is ===>%s" % get_file_name)  # for test

        if get_file_name == "/":
            get_file_name = g_document_root + "/index.html"
        else:
            get_file_name = g_document_root + get_file_name

        print("file name is ===2>%s" % get_file_name) # for test

        try:
            f = open(get_file_name, "rb")
        except IOError:
            response_header = "HTTP/1.1 404 not found\r\n"
            response_header += "\r\n"
            response_body = "====sorry ,file not found===="
        else:
            response_header = "HTTP/1.1 200 OK\r\n"
            response_header += "\r\n"
            response_body = f.read()
            f.close()
        finally:
            self.client_socket.send(response_header.encode('utf-8'))
            self.client_socket.send(response_body)
            self.client_socket.close()


# 设定服务器的端口
g_server_addr = (HOST, PORT) = "", 8888
# 设置服务器服务静态资源时的路径
g_document_root = "./html"


def main():
    httpd = WSGIServer(g_server_addr)
    print("web Server: Serving HTTP on port %d ...\n" % PORT)
    httpd.serve_forever()

if __name__ == "__main__":
    main()

```