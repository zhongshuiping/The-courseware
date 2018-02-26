from gevent import monkey
monkey.patch_all()  # recv recvfrom accept time.sleep
import socket
import re
import gevent
import sys

""""
1.0 不管用户访问什么资源 都返回Helloxxxx
2.0 根据用户访问资源路径 返回响应的数据
3.0 基于多线程实现多任务的web服务器
4.0 基于多进程实现多任务的web服务器
5.0 基于面向对象实现
6.0 协程实现
7.0 使用命令行参数控制 服务器绑定的端口
"""


class HTTPServer(object):
    def __init__(self, port, app):
        """初识化操作"""
        # 1 创建TCP套接字
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2 设置地址重用选项-让服务器重启之后可以理解重新使用绑定的端口
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2 绑定 监听  取客户端
        server_socket.bind(('', port))  #

        server_socket.listen(128)  # 128表示

        self.server_socket = server_socket

        # 保存一个app函数的引用
        self.app = app

    def client_handler(self, client_socket, client_addr):
        """针对每个客户端 使用这个函数进行服务"""
        print("接受到来自%s的连接请求" % str(client_addr))
        # 给client-socket 服务
        # 接收客户端请求报文数据
        recv_data = client_socket.recv(4096)
        # print(recv_data)
        # 将Bytes类型的数据 进行解码 ----> str
        recv_str_data = recv_data.decode()

        # 对请求报文 按行进行切割 返回值就是含有每行数据的 列表   请求行就是列表中0号元素
        data_list = recv_str_data.split('\r\n')
        # print(data_list)

        request_line = data_list[0]
        # print(request_line)

        # 使用正则从 请求行 将用户请求路径 提取出来 GET /index2.html HTTP/1.1
        res = re.match(r"\w+\s+(\S+)", request_line)
        if not res:
            # 匹配失败
            print("HTTP请求报文格式错误")
            client_socket.close()
            return
        # 根据匹配结果对象 获取出用户请求路径信息 在第一个分组
        path_info = res.group(1)
        print("接收到用户的请求:%s" % path_info)  # ./static + /index2.html
        # /home/python/Desktop/key.txt

        # /路径对于web服务器来讲  对应的是首页资源  是web服务器通用的潜规则
        if path_info == '/':
            path_info = '/index.html'
        env = {
            "PATH_INFO": path_info
        }
        # 判断浏览器请求的资源类型 动态 还是 静态
        # 如果是静态请求 走之前web服务器的流程  如果是动态 走动态处理的流程
        # if path_info.endswith(".py"):

        # 实现伪静态的ＵＲＬ　　当用户请求***.html走　动态资源请求的流程
        if path_info.endswith(".html"):

            # app函数返回值就是响应体        HTTP请求相关的字典  函数引用
            response_body = self.app(env, self.start_respose)
            # 拼接响应状态 头部 空行 响应体
            response_data = self.status_header + response_body

            # 发送 关闭
            client_socket.send(response_data.encode())
            client_socket.close()
        else:
            try:
                # 根据用户请求的路径 读取指定路径下的文件数据 将数据 以HTTP响应报文格式发送给浏览器即可
                file = open("./static" + path_info, "rb")

                file_data = file.read()  # bytes
                file.close()
            except FileNotFoundError as e:
                print(e)
                # 用户请求的资源路径不存在 应该返回404 Not Found
                # 响应行
                response_line = "HTTP/1.1 404 Not Found\r\n"

                # 响应头
                response_headers = "Server: PWS4.0\r\n"

                # 响应体
                response_body = "ERROR!!!!!!!!!!"

                response_data = response_line + response_headers + "\r\n"+ response_body

                # send函数的返回值代表 成功发送的字节数----> 可能一下不能全部发送完数据
                client_socket.send(response_data.encode())
            else:
                # 给客户端回HTTP响应报文
                # 响应行
                response_line = "HTTP/1.1 200 OK\r\n"

                # 响应头
                response_headers = "Server: PWS4.0\r\n"

                # 响应体
                response_body = file_data

                # 拼接响应报文  发送给客户端
                response_data = (response_line + response_headers + '\r\n').encode() + response_body
                # send函数的返回值代表 成功发送的字节数----> 可能一下不能全部发送完数据
                # client_socket.send(response_data)
                client_socket.sendall(response_data)

            finally:
                # 关掉套接字
                client_socket.close()

    # "200 OK"  [(,),()()()()]
    def start_respose(self, status, header_list):
        """保存 应用框架提供的状态和响应头"""
        # print("start_response running")
        # print(status)
        # print(header_list)

        # 该属性存储 响应状态和 响应头  在其他方法中使用
        self.status_header = "HTTP/1.1 %s\r\n" % status
        for header_name, header_value in header_list:
            self.status_header += "%s: %s\r\n" % (header_name, header_value)

        # 追加空行
        self.status_header += '\r\n'

    def start(self):
        while True:
            client_socket, client_addr = self.server_socket.accept()
            # 接受一个客户端连接  使用一个协程为客户服务
            gevent.spawn(self.client_handler, client_socket, client_addr)


def main():
    # python3 web.py 8888 Application:app
    if len(sys.argv) != 3:
        print("使用方式错误 python3 web.py 8888 应用框架名:函数名")
        return
    # sys是一个存放 命令行参数 的列表  其中每一个元素是字符串
    # 第0个元素是程序名称 888a
    port = sys.argv[1]
    if not port.isdigit():
        print("端口号只能是数字 ")
        return

    portnumber = int(port)

    module_name_func_name = sys.argv[2]
    # print(sys.argv[2])

    # import Application
    # app = Application.app
    data_list = module_name_func_name.split(":")
    if len(data_list) != 2:
        print("使用方式错误 python3 web.py 8888 应用框架名:函数名")
        return
    module_name = data_list[0]
    func_name = data_list[1]
    try:
        # 返回值是模块对象          参数是模块名<字符串>
        # import threading ====threading = __import__("threading")
        mod = __import__(module_name)
        # app = mod.app 参数1对象 参数2是属性名称  返回值是属性的引用
        app = getattr(mod, func_name)
    except Exception as e:
        print("使用方式错误 python3 web.py 8888 应用框架名:函数名")
        return
    else:
        # port = 8888
        # 创建一个HTTPServer类型的对象
        http_server = HTTPServer(portnumber, app)

        # 启动对象 开始启动HTTP服务
        http_server.start()

        """面向对象 封装 继承 多态"""
        # 狗.吃(翔) =======> 吃(狗,翔)

if __name__ == '__main__':
    main()
    # app函数作用 参数含义 谁提供谁调用
    # start_response函数作用 参数含义 谁提供谁调用
    # app函数返回值意义