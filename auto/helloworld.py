from selenium import webdriver
from time import sleep

d=webdriver.Chrome()
d.get('http://www.baidu.com')
d.find_element_by_id('kw').send_keys('helloworld')
d.find_element_by_id('su').click()
sleep(3)
d.close()
