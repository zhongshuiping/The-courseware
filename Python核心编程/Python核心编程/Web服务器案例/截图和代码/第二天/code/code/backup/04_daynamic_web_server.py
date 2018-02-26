# coding:utf-8

import socket
import re
import sys

from multiprocessing import Process

# 设置静态文件根目录
HTML_ROOT_DIR = "./html"
PYTHON_ROOT_DIR = "./wsgibins"


class HTTPServer(object):
    """"""
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def bind(self, address):
        self.server_socket.bind(address)

    def start(self):
        self.server_socket.listen(128)

        while True:
            client_socket, client_address = self.server_socket.accept()
            # print("[%s, %s]用户连接上了" % (client_address[0],client_address[1]))
            print("[%s, %s]用户连接上了" % client_address)
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

    def start_response(self, status, headers):
        server_headers = [
            ("Server", "My Server")
        ]
        self.headers_set = [status, server_headers+headers]

    def handle_client(self, client_socket):
        """处理客户端请求"""
        # 获取客户端请求数据
        request_data = client_socket.recv(1024)
        print("request data:", request_data)
        request_lines = request_data.splitlines()
        for line in request_lines:
            print(line)

        # 解析请求报文
        # 'GET / HTTP/1.1'
        request_start_line = request_lines[0]
        # 提取用户请求的文件名
        print("*"*10)
        print(request_start_line.decode("utf-8"))
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)

        if "/" == file_name:
            file_name = "/index.html"

        if file_name.endswith(".py"):
            module_name = file_name[1:-3]
            try:
                m = __import__(module_name)
            except Exception:
                self.headers_set = ["404 Not Found"]
                response_body = "sorry, not found"
            else:
                app = getattr(m, "application")
                environ = {}
                response_body = app(environ, self.start_response)
            response = "HTTP/1.1 " + self.headers_set[0] + "\r\n"
            if len(self.headers_set)>1:
                for header in self.headers_set[1]:
                    response += "%s: %s\r\n" % header
            response += "\r\n"
            response += response_body

        else:
            # 打开文件，读取内容
            try:
                file = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                response_start_line = "HTTP/1.1 404 Not Found\r\n"
                response_headers = "Server: My server\r\n"
                response_body = "The file is not found!"
            else:
                file_data = file.read()
                file.close()

                # 构造响应数据
                response_start_line = "HTTP/1.1 200 OK\r\n"
                response_headers = "Server: My server\r\n"
                response_body = file_data.decode("utf-8")

            response = response_start_line + response_headers + "\r\n" + response_body
            print("response data:", response)

        # 向客户端返回响应数据
        client_socket.send(bytes(response, "utf-8"))

        # 关闭客户端连接
        client_socket.close()


def main():
    sys.path.insert(1, PYTHON_ROOT_DIR)
    server = HTTPServer()
    server.bind(("", 8000))
    server.start()


if __name__ == "__main__":
    main()
