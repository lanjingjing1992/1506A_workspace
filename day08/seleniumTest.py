#coding=utf-8
from selenium import webdriver
import unittest
from time import sleep
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

class Baidu(unittest.TestCase):
    def setUp(self):#初始化的方法
        self.driver=webdriver.Chrome()#谷歌浏览器
        self.url='http://www.baidu.com'
        self.exceptions=[]
    def testSearch(self):
        d=self.driver#区分局部变量跟属性的用法
        d.get(self.url)#打开网址
        d.find_element_by_id('kw').send_keys('selenium')#输入框
        d.find_element_by_id('su').click()

    def testLogin(self):
        d=self.driver
        d.get(self.url)
        d.find_element_by_xpath('//*[@id="u1"]/a[7]').click()#登陆
        d.implicitly_wait(30)
        d.switch_to_alert()
        try:
            d.find_element_by_xpath('//*[@id="pass_phoenix_btn"]/ul/li[1]/a').click()#qq登陆
        except Exception,e:
            self.exceptions.append(e)

        all_windows=d.window_handles#存储的所有的窗口
        current_window=d.current_window_handle#当前的窗口
        for window in all_windows:
            if window!=current_window:#新的窗口
                d.switch_to_window(window)#跳转窗口
        d.switch_to_frame('ptlogin_iframe')
        d.find_element_by_id('img_out_2364365304').click()
    def tearDown(self):
        if len(self.exceptions)!=0:
            file=open('test.txt','w+')
            file.write(str(self.exceptions))
            file.close()
        self.driver.quit()

if __name__ == '__main__':
    suite=unittest.TestSuite()#创建测试集合
    suite.addTest(Baidu('testSearch'))
    suite.addTest(Baidu('testLogin'))
    # unittest.main(defaultTest='suite')
    runner=HTMLTestRunner(stream=open('result.html','w+'),title='lanjingjing',description='this is lanjingjing result')
    runner.run(suite)






