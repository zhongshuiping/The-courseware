import socket

""""
1 浏览器-------HTTP请求--->HTTP服务器
       <------HTTP响应-------------

"""


# 1 创建TCP套接字  IPv4地址协议族  流式报文协议
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 输入需要访问的网址  ----DNS----> IP
# 3 建立和服务器的连接 (发起三次握手)
tcp_socket.connect(('itcastcpp.cn', 80))

# 4 发送HTTP请求报文《HTTP请求报文格式》
#   请求行 + 请求头 + 空行
request_line = "GET / HTTP/1.1\r\n"
request_header = "Host: itcastcpp.cn\r\n"
request_data = request_line + request_header + "\r\n"
tcp_socket.send(request_data.encode())

# 5 模拟浏览接收HTTP响应报文
response_data = tcp_socket.recv(4096)
print(response_data)

# 6 关闭套接字
tcp_socket.close()
