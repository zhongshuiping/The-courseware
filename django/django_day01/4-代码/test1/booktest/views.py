from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
# Create your views here.

# 定义视图函数
# url配置: 建立url地址和视图函数之间的对应关系
# 1.在项目的urls文件中包含应用的urls文件
# 2.在应用的urls文件配置url地址和视图的对应关系
# url配置时需要严格匹配开头和结尾
# /index


def my_render(request, template_path, context={}):
    # 1.加载模板文件，获取模板对象, 返回Template
    temp = loader.get_template(template_path)
    # 2.定义模板上下文，给模板文件传递数据
    context = RequestContext(request, context)
    # 3.模板渲染: 把模板变量替换成对应的值
    res_html = temp.render(context)
    print(res_html)

    # 4. 返回html内容
    return HttpResponse(res_html)


def index(request):
    # 进行处理
    # 老铁，没毛病
    '''
    <html>
        <head>
            <title></title>
        </head>
        <body></body>
    </html>
    '''
    # return HttpResponse('老铁，没毛病')

    # 使用模板文件
    # # 1.加载模板文件，获取模板对象, 返回Template
    # temp = loader.get_template('booktest/index.html')
    # # 2.定义模板上下文，给模板文件传递数据
    # context = RequestContext(request, {'content': 'hello python', 'my_list': list(range(1, 10))})
    # # 3.模板渲染: 把模板变量替换成对应的值
    # res_html = temp.render(context)
    # print(res_html)
    #
    # # 4. 返回html内容
    # return HttpResponse(res_html)

    # return my_render(request, 'booktest/index.html', {'content': 'hello python', 'my_list': list(range(1, 10))})
    return render(request, 'booktest/index.html', {'content': 'hello python', 'my_list': list(range(1, 10))})


# /index2
def index2(request):
    return HttpResponse('index2')