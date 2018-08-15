#coding=utf-8
#athor: Yunlian
#date: 0818-3
import unittest,os
#这里需要导入测试文件
import test_case.baidu
import test_case.youdao
import HTMLTestRunner

testunit=unittest.TestSuite()
#将测试用例加入到测试容器(套件)中
#Demo_unittest.Unittest.search.test_case.baidu.Baidu对应的是unittest框架下的类
testunit.addTest(unittest.makeSuite(test_case.baidu.Baidu))
# testunit.addTest(unittest.makeSuite(Demo_unittest.Unittest.search.test_case.youdao.Youdao))
#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testunit)
#定义个报告存放路径，支持相对路径。
test_report_dir=os.getcwd()+r'\report'
isExists=os.path.exists(test_report_dir)
if not isExists:
    # 如果不存在则创建目录
    # 创建目录操作函数
    os.makedirs(test_report_dir)
filename = test_report_dir+'\\'+'result.html'
fp = open(filename, 'wb')

runner =HTMLTestRunner.HTMLTestRunner(
stream=fp,
title=u'搜索网站测试报告',
description=u'用例执行情况：')

#执行测试用例
runner.run(testunit)
