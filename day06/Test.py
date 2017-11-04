#coding=utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains#鼠标事件
from selenium.webdriver.common.keys import Keys#键盘事件

d=webdriver.Chrome()

#打开百度网址
d.get('https://qzone.qq.com/')
#百度页面点击新闻
# d.find_element_by_link_text('新闻').click()#点击新闻
# sleep(2)
# d.back()
# sleep(2)
# d.close()#关闭
#百度页面点击设置
# set=d.find_element_by_xpath('//*[@id="u1"]/a[8]')#设置的元素
# ActionChains(d).click_and_hold(set).perform()
# sleep(2)
#点击搜索设置
# d.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()
# sleep(2)
# # d.close()
# #保存设置
#获取一组元素
# ths=d.find_elements_by_tag_name('th')
# print type(ths)

# for th in ths:#遍历元素
#     print th.text
# d.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()
# sleep(2)
#获取弹出框
# alert=d.switch_to_alert()#弹出框
# sleep(2)
#点击确定
# alert.accept()#确定
# more=d.find_element_by_xpath('//*[@id="u1"]/a[9]')
#点击更多产品
# ActionChains(d).click_and_hold(more).perform()
#点击糯米
# d.find_element_by_link_text('糯米').click()
# sleep(2)
# d.back()#回退
#邮箱账号登陆163邮箱
# login=d.find_element_by_xpath('//*[@id="lbNormal"]')
#
# ActionChains(d).click_and_hold(login).perform()#鼠标事件
# sleep(2)
#进入到iframe层  就像一个箱子 里面是需要获取的元素 需要先切入到iframe里面
# d.switch_to_frame('x-URS-iframe')
# d.find_element_by_name('email').send_keys('15901337131')
# d.find_element_by_name('password').send_keys('123456')
# d.find_element_by_id('dologin').click()
#qq空间登陆
d.switch_to_frame('login_frame')#切入到iframe
#账号密码登陆
d.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
#账号
name=d.find_element_by_xpath('//*[@id="u"]')
name.send_keys('2364365304')
name.send_keys(Keys.TAB)#键盘事件换行
#密码
pw=d.find_element_by_xpath('//*[@id="p"]')
pw.send_keys('123456')
# pw.send_keys(Keys.ENTER)#键盘事件登陆
#登陆
d.find_element_by_id('login_button').click()
sleep(5)
