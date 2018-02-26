from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from booktest.models import BookInfo
from datetime import date
# Create your views here.


# /index
def index(request):
    """首页"""
    # 1. 获取所有图书的信息
    books = BookInfo.objects.all()

    # 2. 使用模板
    return render(request, 'booktest/index.html', {'books': books})


# /create
def create(request):
    """添加图书"""
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1991, 1, 1)
    # 添加进数据库
    b.save()

    # return HttpResponse('添加成功')
    # 重定向访问/index
    # return HttpResponseRedirect('/index')
    return redirect('/index')


# /delete图书id
def delete(request, bid):
    """删除图书"""
    # 根据bid查找图书
    b = BookInfo.objects.get(id=bid)

    # 删除图书
    b.delete()

    # 重定向到/index
    # return HttpResponseRedirect('/index')
    return redirect('/index')











