import time

def get_time():
    return time.ctime()

def app(environ, start_response2):
    """当web服务器收到动态资源请求的时候 会调用该函数来执行"""
    # envrion是一个字典 存储的就是客户端的HTTP请求相关的键值对
    # PATH_INFO表示用户请求路径
    # start_response就是web服务器传递给应用程序使用的一个函数的引用

    path_info = environ['PATH_INFO']
    print("收到动态资源请求路径是%s" % path_info)

    if path_info == '/gettime.py':
        start_response2('200 OK', [('Content-Type', 'text/html')])
        return get_time()
    else:
        # start_response就是用来设置响应状态和响应头的函数
        start_response2('404 Not Found', [('Content-Type', 'text/html')])

        # app函数的返回值就是响应体
        return 'Hello World!'