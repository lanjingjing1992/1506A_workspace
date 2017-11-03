#coding=utf-8
from time import sleep
from selenium import webdriver #驱动
d=webdriver.Chrome()

d.get('http://172.16.10.119:8080/bwie/')
# d.implicitly_wait(30)
print d.title
# d.find_element_by_id('kw').send_keys('selenium')#输入内容
# d.find_element_by_id('su').click()#点击
# sleep(3)
# print d.title

# cp=d.find_element_by_id('cp')
#
# sleep(2)
# print cp
# sleep(2)
# print cp.text
# d.close()
# d.set_window_size(480,800)#设置浏览器窗口大小
# sleep(2)
# d.maximize_window()#最大化
# sleep()
# d.close()
# d.find_element_by_id('username').send_keys('lanjingjing')
# d.find_element_by_id('password').send_keys('442131ljj')
# d.find_element_by_link_text('登陆').click()
d.find_element_by_link_text('集团动态').click()
sleep(2)
d.find_element_by_link_text('下一页').click()
sleep(2)
d.find_element_by_partial_link_text('八维年度安全稳定').click()
sleep(2)
d.back()
sleep(2)

d.close()