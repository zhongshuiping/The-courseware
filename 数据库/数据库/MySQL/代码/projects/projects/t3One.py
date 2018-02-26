#coding=utf-8
import MySQLdb

try:
    conn=MySQLdb.connect(host="localhost",port=3306,db='test2',user='root',passwd='mysql',charset='utf8')
    cs1=conn.cursor()

    # row=cs1.execute('select count(*) from stu')
    #
    # # print row
    # # print cs1
    #
    # stu=cs1.fetchone()
    # print stu[0]

    cs1.execute('select name,gender from stu')
    rows=cs1.fetchall()
    # print rows
    for row in rows:
        print type(row[1])

    cs1.close()
    conn.close()
except Exception,e:
    print e



