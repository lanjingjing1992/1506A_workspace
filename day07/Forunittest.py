#coding=utf-8
import unittest
from selenium import webdriver

class Baidu(unittest.TestCase):
    def setUp(self):#重写方法
        self.driver=webdriver.Chrome()#属性
        self.url='http://www.baidu.com'#属性

    def testOpen(self):
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()








