#coding=utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains#鼠标事件

d=webdriver.Chrome()

#打开百度网址
d.get('http://mail.163.com/')
# d.find_element_by_link_text('新闻').click()#点击新闻
# sleep(2)
# d.back()
# sleep(2)
# d.close()#关闭
# set=d.find_element_by_xpath('//*[@id="u1"]/a[8]')#设置的元素
# ActionChains(d).click_and_hold(set).perform()
# sleep(2)
# d.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()#点击搜索设置
# sleep(2)
# # d.close()
# #保存设置
# ths=d.find_elements_by_tag_name('th')
# print type(ths)
# for th in ths:#遍历
#     print th.text
# d.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()
# sleep(2)
# alert=d.switch_to_alert()#弹出框
# sleep(2)
# alert.accept()#确定
# more=d.find_element_by_xpath('//*[@id="u1"]/a[9]')
# ActionChains(d).click_and_hold(more).perform()#点击更多产品
# d.find_element_by_link_text('糯米').click()#点击糯米
# sleep(2)
# d.back()#回退
#邮箱账号登陆
login=d.find_element_by_xpath('//*[@id="lbNormal"]')

ActionChains(d).click_and_hold(login).perform()#鼠标事件
sleep(2)
d.switch_to_frame('x-URS-iframe')
d.find_element_by_name('email').send_keys('15901337131')
d.find_element_by_name('password').send_keys('123456')
d.find_element_by_id('dologin').click()