#coding=utf-8
import MySQLdb

try:
    conn=MySQLdb.connect(host='localhost',port=3306,db='test2',user='root',passwd='mysql',charset='utf8')
    cs1=conn.cursor()

    uname=raw_input("请输入用户名：")
    ubirthday=raw_input("请输入生日：")
    ugender=raw_input("请输入性别：")
    params=[uname,ubirthday,int(ugender),10]
    sql="update stu set name=%s,birthday=%s,gender=%s where id=%s"
    cs1.execute(sql,params)

    #insert

    #delete
    conn.commit()
    cs1.close()
    conn.close()
    print 'ok'
except Exception,e:
   print e
   conn.rollback()
