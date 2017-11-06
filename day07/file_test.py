#coding=utf-8
file=open('test.txt','w+')#以w+模式打开文件
file.write('helloworld')#写入helloworld
file.seek(0,0)#把游标放到最前面
data=file.read()#读取三个字符
print data
file.close()#关闭文件