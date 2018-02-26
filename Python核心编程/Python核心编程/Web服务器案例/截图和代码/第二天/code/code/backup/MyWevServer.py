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
    def __init__(self, application):
        self.app = application
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

        environ = {
            "PATH_INFO":file_name
        }
        response_body = self.app(environ, self.start_response)
        response = "HTTP/1.1 " + self.headers_set[0] + "\r\n"
        if len(self.headers_set)>1:
            for header in self.headers_set[1]:
                response += "%s: %s\r\n" % header
        response += "\r\n"
        response += response_body

        # 向客户端返回响应数据
        client_socket.send(bytes(response, "utf-8"))

        # 关闭客户端连接
        client_socket.close()


def main():
    # sys.path.insert(1, PYTHON_ROOT_DIR)
    if len(sys.argv)<2:
        sys.exit()
    web_module_name, web_application_name = sys.argv[1].split(":")
    web_module = __import__(web_module_name)
    web_application = getattr(web_module, web_application_name)
    app = web_application()
    server = HTTPServer(app)
    server.bind(("", 8000))
    server.start()


if __name__ == "__main__":
    main()
