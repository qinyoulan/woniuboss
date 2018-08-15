#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

#百度搜索用例
    def test_baidu_search(self):
        #print("test query test case")
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        # driver.quit()

#百度设置用例
    def test_baidu_set(self):
        #print("test baidu begin")
        driver = self.driver
    #进入搜索设置页
        driver.get(self.base_url + "/gaoji/preferences.html")
    #设置每页搜索结果为 50 条
        m=driver.find_element_by_name("NR")
        m.find_element_by_xpath("//option[@value='50']").click()
        time.sleep(2)
    #保存设置的信息
        driver. find_element_by_xpath("//input[@value='保存设置']").click()
        time.sleep(2)
        driver.switch_to_alert().accept()

    def tearDown(self):
        self.driver.close()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Baidu('test_baidu_search'))

    runner = unittest.TextTestRunner()
    runner.run(suite)

#使用她可以方便的将一个单元测试模块变为可直接运行的测试脚本，main()方法使用TestLoader类来搜索所有包含在该模块中以“test”命名开头的测试方法，
# 并自动执行他们。执行方法的默认顺序是：根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0-9，A-Z，a-z。所以以A开头的测试用例方法会优先执行，以a开头会后执行。
    # unittest.main()