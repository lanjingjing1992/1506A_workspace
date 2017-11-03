#coding=utf-8
from time import sleep
from selenium import webdriver #驱动
d=webdriver.Chrome()

d.get('http://www.baidu.com')

d.find_element_by_id('kw').send_keys('selenium')#输入内容
d.find_element_by_id('su').click()#点击


sleep(2)
d.close()