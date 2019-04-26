#  coding utf-8
# @time      :2019/4/2415:11
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_VehicleManagement.py
from selenium import webdriver

from WEB_Framework.PageObject.login_page import LoginPage
from WEB_Framework.Testdatas import common_data as cd
from WEB_Framework.PageObject.VehicleManagement import vehicleManagement
from WEB_Framework.PageObject.index_page import IndexPage


import unittest

class vehicle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service_log_path=r"D:\ChromeLog\log.log")
        cls.driver.maximize_window()
        cls.driver.get(cd.login_url)
        LoginPage(cls.driver).Login(cd.username,cd.pwd,cd.code)




    def tearDownClass(cls):
        cls.driver.quit()

    def test_VehicleDetails(self):
        vehicleManagement(self.driver).Management()
        self.assertTrue(IndexPage(self.driver).vehicleManagement_Exists())






