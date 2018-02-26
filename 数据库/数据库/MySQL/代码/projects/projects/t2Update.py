#encoding=utf8
import MySQLdb
try:
    conn=MySQLdb.connect(host='localhost',port=3306,db='test2',user='root',passwd='mysql',charset='utf8')
    cs1=conn.cursor()
    a=cs1.execute('update stu set name="李四" where name="张三"')
    print a
    conn.commit()
    cs1.close()
    conn.close()
except Exception,e:
    print e
