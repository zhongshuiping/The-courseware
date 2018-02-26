#coding=utf-8
from MysqlHelper import MysqlHelper
from hashlib import sha1

#注册
# uname=raw_input("请输入用户名：")
# upwd=raw_input("请输入密码：")
#
# s1=sha1()
# s1.update(upwd)
# upwd2=s1.hexdigest()
#
# sql='insert into users(uname,upwd) values(%s,%s)'
# params=[uname,upwd2]
#
# helper=MysqlHelper()
# row=helper.insert(sql,params)
# print row

#登录
uname=raw_input("请输入用户名：")
upwd=raw_input("请输入密码：")

s1=sha1()
s1.update(upwd)
upwd2=s1.hexdigest()

sql="select upwd from users where uname=%s"
params=[uname]

helper=MysqlHelper()
result=helper.fetchone(sql,params)
if result==None:
    print '用户名错误'
elif result[0]==upwd2:
    print '登录成功'
else:
    print '密码错误'
