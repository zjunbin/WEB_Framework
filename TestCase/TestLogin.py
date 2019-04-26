#  coding utf-8
# @time      :2019/4/2316:39
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :TestLogin.py
from selenium import webdriver
from WEB_Framework.PageObject.login_page import LoginPage
from WEB_Framework.PageObject.index_page import IndexPage
from WEB_Framework.Testdatas import common_data as cd
from WEB_Framework.Testdatas import login_datas as ld
from ddt import ddt,data
import unittest
import time

datacase=[
    {'username':"",'pwd':'123456','code':'123456','excepted':'账号不能为空!'},
    {'username': "adf955", 'pwd': '','code':'123456','excepted':'密码不能为空!'},
    {'username':"888888",'pwd':'123456','code':'','excepted':'验证码不能为空!'},
    {'username':"888888",'pwd':'123456','code':'adfgf','excepted':'验证码为数字，并且必须是5位'}
]
dataerror=[
    {'username':"888888",'pwd':'655444','code':'123456','excepted':'抱歉，账号或密码错误！'},
    {'username': "dfadfaf", 'pwd': '123456','code':'123456','excepted':'抱歉，账号或密码错误！'},
    {'username':"adffdsa",'pwd':'5466544','code':'123456','excepted':'抱歉，账号或密码错误！'}
]


# @ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service_log_path=r"D:\ChromeLog\log.log")
        self.driver.maximize_window()
        self.driver.get(cd.login_url)


    def tearDown(self):
        self.driver.quit()
        # time.sleep(0.5)
        # self.driver.refresh()
        # time.sleep(1)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    def test_login_3(self):
        LoginPage(self.driver).Login(ld.success_data['username'],ld.success_data['pwd'],ld.success_data['code'])
        print(IndexPage(self.driver).isExist_quitEle())
        self.assertTrue(IndexPage(self.driver).isExist_quitEle())

    # @data(*ld.datacase)
    # def test_login1_error(self,item):
    #     LoginPage(self.driver).Login(item['username'],item['pwd'],item['code'])
    #     self.assertEqual(item['excepted'],LoginPage(self.driver).get_find_from_loginArea())
    #
    # @data(*ld.dataerror)
    # def test_login2_error(self, item):
    #     LoginPage(self.driver).Login(item['username'], item['pwd'], item['code'])
    #     self.assertEqual(item['excepted'], LoginPage(self.driver).get_error())


