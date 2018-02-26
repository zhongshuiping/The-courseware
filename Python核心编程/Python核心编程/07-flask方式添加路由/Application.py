import time
import re


# 创建一个列表 存储的所有的路径及其对应的函数代码 -- 路由列表 flask添加方法
routing_list = [
    # ('/gettime.py', get_time),
    # ('/index.py', index),
    # ('/center.py', center)
]


def route(path):
    def warpper(func):
        #　将路由信息添加进列表中
        routing_list.append((path, func))
        def inner(*args, **kwargs):
            return func()
        return inner
    return warpper

# 为什么下面这一行代码能够将　路由信息添加到列表中?????
@route("/gettime.py")
def get_time():
    return time.ctime()


@route("/index.py")
def index():
    # 读取模板文件　
    with open("template/" + "index.html") as file:
        file_data = file.read()
    # 替换
    data = "这是测试数据"
    html_data = re.sub(r"\{%content%\}", data, file_data)

    # 返回替换之后的数据
    return html_data


@route('/center.py')
def center():
    # 读取模板文件　
    with open("template/" + "center.html") as file:
        file_data = file.read()
    # 替换
    data = "这是测试数据"
    html_data = re.sub(r"\{%content%\}", data, file_data)

    # 返回替换之后的数据
    return html_data

"""思考路由列表的作用(对比没有路由列表的情况)"""

def app(environ, start_response2):
    """当web服务器收到动态资源请求的时候 会调用该函数来执行"""
    # envrion是一个字典 存储的就是客户端的HTTP请求相关的键值对
    # PATH_INFO表示用户请求路径
    # start_response就是web服务器传递给应用程序使用的一个函数的引用

    path_info = environ['PATH_INFO']
    print("收到动态资源请求路径是%s" % path_info)

    # if path_info == '/gettime.py':
    #     start_response2('200 OK', [('Content-Type', 'text/html')])
    #     return get_time()
    # elif path_info == '/index.py':
    #     start_response2('200 OK', [('Content-Type', 'text/html')])
    #     return index()
    # elif path_info == '/center.py':
    #     start_response2('200 OK', [('Content-Type', 'text/html')])
    #     return center()
    for path,func in routing_list:
        # 遍历路由列表 判断其中某一项数据是否和用户请求的路径匹配
        if path == path_info:
            start_response2('200 OK', [('Content-Type', 'text/html')])
            return func()
    else:
        # start_response就是用来设置响应状态和响应头的函数
        start_response2('404 Not Found', [('Content-Type', 'text/html')])

        # app函数的返回值就是响应体
        return 'Hello World!'