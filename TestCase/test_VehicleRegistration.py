#  coding utf-8
# @time      :2019/4/2515:10
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_VehicleRegistration.py
from selenium import webdriver
import unittest


from WEB_Framework.PageObject.login_page import LoginPage
from WEB_Framework.Testdatas import common_data as cd
from WEB_Framework.PageObject.vehicleregistration import vehicleregistration
from WEB_Framework.PageObject.index_page import IndexPage
from WEB_Framework.Testdatas import Registration_use_case as rg
from ddt import ddt,data

@ddt
class Registration(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome(service_log_path=r"D:\ChromeLog\log.log")
    #     cls.driver.maximize_window()
    #     cls.driver.get(cd.login_url)
    #     LoginPage(cls.driver).Login(cd.username,cd.pwd,cd.code)

    # def tearDownClass(cls):
    #     cls.driver.quit()
    def setUp(self):
        self.driver = webdriver.Chrome(service_log_path=r"D:\ChromeLog\log.log")
        self.driver.maximize_window()
        self.driver.get(cd.login_url)
        LoginPage(self.driver).Login(cd.username,cd.pwd,cd.code)

    def tearDown(self):
        self.driver.quit()

    #进入车辆登记页面
    def test_registration1(self):
        vehicleregistration(self.driver).registrationPage()
        self.assertTrue(IndexPage(self.driver).vehicleManagement_Exists())

    #正常的车辆信息登记
    def test_registration2(self):
        vehicleregistration(self.driver).registrationPage()
        vehicleregistration(self.driver).NewVehicle(rg.success_data['txtOwnName'],rg.success_data['txtIDCardNumber'],
                                                    rg.success_data['txtOwnTel'],rg.success_data['txtVIN'],
                                                    rg.success_data['txtBrand'],rg.success_data['txtMotorNumber'],
                                                    rg.success_data['txtColor'])
        self.assertEqual(rg.success_data['exp'],vehicleregistration(self.driver).SuccessfulRegistration())

    #空数据异常信息登记
    @data(*rg.error_data)
    def test_registration3(self,item):
        vehicleregistration(self.driver).registrationPage()
        vehicleregistration(self.driver).NewVehicle(item['txtOwnName'],item['txtIDCardNumber'],
                                                    item['txtOwnTel'],item['txtVIN'],
                                                    item['txtBrand'],item['txtMotorNumber'],
                                                    item['txtColor'])
        self.assertEqual(item['exp'], vehicleregistration(self.driver).ErrorRegistration())

    #删除用户信息
    def test_registration4(self):
        vehicleregistration(self.driver).registrationPage()

        vehicleregistration(self.driver).Del_data()
        self.assertEqual('当前没有车辆信息',vehicleregistration(self.driver).Number_elements())

