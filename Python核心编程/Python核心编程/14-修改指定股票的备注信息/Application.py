import time
import re
from pymysql import connect

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
@route("/gettime.html")
def get_time(path_info):
    return time.ctime()


@route("/index.html")
def index(path_info):
    # 读取模板文件　
    with open("template/" + "index.html") as file:
        file_data = file.read()
    # 连接数据库　查询结果
    try:
        conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cursor = conn.cursor()
        sql = """select * from info;"""
        cursor.execute(sql)
        # ((一行数据),(一行记录))
        data_set = cursor.fetchall()
        data = ""
        # (1, '000007', '全新好', '10.01%', '4.40%', Decimal('16.05'), Decimal('14.60'), datetime.date(2017, 7, 18))
        for line in data_set:
            # data += str(line)
            line_str = """<tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s"></td>
            </tr>""" % (line[0], line[1], line[2], line[3], line[4],line[5], line[6], line[7], line[1])
            data += line_str

        conn.commit()
    except Exception as e:
        conn.rollback()
        return "失败" + str(e)
    else:
        # 替换数据
        html_data = re.sub(r"\{%content%\}", data, file_data)
        return html_data
    finally:
        cursor.close()
        conn.close()


@route('/center.html')
def center(path_info):
    # 读取模板文件　
    with open("template/" + "center.html") as file:
        file_data = file.read()
    # 连接数据库
    try:
        conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cursor = conn.cursor()
        sql = """select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info  from focus f join info i on f.info_id = i.id;"""
        cursor.execute(sql)
        data = ""

        # ('300268', '万福生科', '-10.00%', '0.27%', Decimal('31.77'), Decimal('13.57'), '你确定要买这个？')
        for line in cursor.fetchall():
            # data += str(line)
            data_line = """<tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a></td>
                <td> <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s"></td>
                </tr>
            """ % (line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[0],line[0])
            data += data_line
        conn.commit()
    except Exception as e:
        conn.rollback()
        return "失败" + str(e)
    else:
        html_data = re.sub(r"\{%content%\}", data, file_data)
        # 返回替换之后的数据
        return html_data
    finally:
        cursor.close()
        conn.close()

# /add/000007.html
# /add/000036.html   /add/\d{6}.html


@route(r"^/add/(\d{6})\.html$")
def add(path_info):
    """添加指定的某只股票到收藏夹中"""
    print("in add %s" % path_info)
    res = re.match(r"^/add/(\d{6})\.html$", path_info)
    # 根据正则获取到股票代码
    stock_code = res.group(1)

    try:
        conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cursor = conn.cursor()
        # 判断需要插入的股票在收藏夹中是否存在
        sql = """select id from focus where info_id = (select id from info where code=%s)"""
        count = cursor.execute(sql, [stock_code])
        if count > 0:
            return "已经添加过了　不必再次添加"

        # 将指定股票代码的数据插入到收藏夹表中
        sql = """insert into focus (info_id) select id from info where code = %s;"""
        cursor.execute(sql, [stock_code])
        conn.commit()
    except Exception as e:
        conn.rollback()
        return "添加收藏失败" + str(e)
    else:
        return "添加收藏成功"
    finally:
        cursor.close()
        conn.close()

# /del/000007.html
@route(r"^/del/(\d{6})\.html$")
def delete(path_info):
    print("in delete %s" % path_info)
    # 根据正则获取到需要删除的股票代码
    res = re.match(r"^/del/(\d{6})\.html$", path_info)
    stock_code = res.group(1)

    try:
        conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cursor = conn.cursor()
        sql = """delete from focus where info_id = (select id from info where code = %s);"""
        count = cursor.execute(sql, [stock_code])
        if count == 0:
            return "股票信息不存在　不需要删除"

        conn.commit()
    except Exception as e:
        conn.rollback()
        return "删除失败" + str(e)
    else:
        return "删除成功"
    finally:
        cursor.close()
        conn.close()

# /update/601918.html
# /update/000007.html

@route(r"/update/(\d{6})\.html")
def update(path_info):
    """显示修改备注的页面"""
    # 根据正则获取到用户需要操作的股票代码
    res = re.match(r"/update/(\d{6})\.html", path_info)
    stock_code = res.group(1)

    try:
        conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cursor = conn.cursor()
        sql = """select note_info from focus where info_id = (select id from info where code = %s);"""
        cursor.execute(sql, [stock_code])

        # 取出的结果就是(备注信息,)
        note_info = cursor.fetchone()[0]

        conn.commit()
        # 读取模板文件
        with open("template/update.html") as file:
            html_data = file.read()

    except Exception as e:
        conn.rollback()
        return "失败" + str(e)
    else:

        # 替换模板
        # 返回替换之后的数据 替换股票代码　　替换备注信息
        html_data = re.sub("{%code%}", stock_code, html_data)
        html_data = re.sub("{%note_info%}", note_info, html_data)
        return html_data
    finally:
        cursor.close()
        conn.close()

# /update/000007/fine.html

@route(r"/update/(\d{6})/(\S+)\.html")
def upadet_note_info(path_info):
    """更新指定股票的备注信息"""
    # 根据正则提取股票代码　新的备注信息
    res = re.match(r"/update/(\d{6})/(\S+)\.html", path_info)
    stock_code = res.group(1)  # 股票代码
    new_note_info = res.group(2)  # 新的备注信息

    # 连接数据库
    # ｓｑｌ 更新指定股票的备注信息
    try:
        conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
        cursor = conn.cursor()
        sql = """ update focus set note_info= %s where info_id = (select id from info where code =%s);"""
        cursor.execute(sql, [new_note_info, stock_code])
        
        conn.commit()
    except Exception as e:
        conn.rollback()
        return "更新备注失败" + str(e)
    else:
        return "更新备注成功"
    finally:
        cursor.close()
        conn.close()


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
        # /add/000036.html == '/add/\d{6}\.html'

        # 由于路由列表中的路径有可能是正则表达式　　不能直接判断是否完全相等
        # if path == path_info:
        if re.match(path, path_info):
            start_response2('200 OK', [('Content-Type', 'text/html')])
            return func(path_info)
    else:
        # start_response就是用来设置响应状态和响应头的函数
        start_response2('404 Not Found', [('Content-Type', 'text/html')])

        # app函数的返回值就是响应体
        return 'Hello World!'