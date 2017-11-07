#coding=utf-8
from selenium import webdriver
import time
import unittest

class Baidu(unittest.TestCase):
    def setUp(self):
        #初始化的方法
        self.driver=webdriver.Chrome()
        self.baiduUrl='http://www.baidu.com'
        self.exceptions=[]
    def testSearch(self):
        #测试方法体
        d=self.driver
        try:
            d.get(self.baiduUrl)
            d.find_element_by_id('kw').send_keys('八维')
            d.find_element_by_id('su').click()
        except Exception,e:
            self.exceptions.append(e)


    def testYoudao(self):
        d=self.driver
        d.get('http://dict.youdao.com/')
    def testQzone(self):
        d=self.driver

        d.get('https://qzone.qq.com/')#打开qq空间
        d.switch_to_frame('login_frame')
        d.find_element_by_id('switcher_plogin').click()
        d.find_element_by_id('u').send_keys('23643653034')#输入qq号
        d.find_element_by_id('p').send_keys('123456')#密码
        d.find_element_by_id('login_button').click()#点击登陆

    def tearDown(self):
        #退出浏览器
        if len(self.exceptions)!=0:
            print self.exceptions
        self.driver.quit()

if __name__ == '__main__':
    pass





