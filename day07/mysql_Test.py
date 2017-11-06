#coding=utf-8
import pymysql
from day07.file_test import FIleIoTest
db=pymysql.connect(host='60.205.189.12',user='visitor',passwd='123456',port=3306)#连接数据库
cursor=db.cursor()#用来进行操作数据库
# cursor.execute('show databases')
# datas= cursor.fetchall()#打印所有的数据
# for  i in datas:#遍历
#     print i
cursor.execute('use 1510f')
cursor.execute('select * from lanjingjing')
datas=cursor.fetchall()#获取全部数据
for i in datas:
    file=FIleIoTest()
    print type(i)#元组类型
    file.inputMenu(str(i))#转换成字符串