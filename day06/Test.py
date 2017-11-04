#coding=utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains#鼠标事件

d=webdriver.Chrome()

#打开百度网址
d.get('http://www.baidu.com')
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
more=d.find_element_by_xpath('//*[@id="u1"]/a[9]')
ActionChains(d).click_and_hold(more).perform()#点击更多产品
d.find_element_by_link_text('糯米').click()#点击糯米
sleep(2)
d.back()#回退