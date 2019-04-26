#  coding utf-8
# @time      :2019/4/2515:10
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :vehicleregistration.py
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

class vehicleregistration:

    def __init__(self,driver):
        self.driver = driver

    #进入登记页面
    def registrationPage(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//img[@id='morefun']")))
        self.driver.find_element(By.XPATH, "//img[@id='morefun']").click()
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, "//div[@id='divMenu_Icon']//a[@rel='251']")))
        self.driver.find_element(By.XPATH, "//div[@id='divMenu_Icon']//a[@rel='251']").click()

    #新增信息
    def NewVehicle(self,txtOwnName,txtIDCardNumber,txtOwnTel,txtVIN,txtBrand,txtMotorNumber,txtColor):
        WebDriverWait(self.driver, 20).until(ec.frame_to_be_available_and_switch_to_it("251"))
        WebDriverWait(self.driver,20).until(ec.frame_to_be_available_and_switch_to_it("bicycleregifr"))

        self.driver.find_element_by_xpath("//input[@id='btnAdd']").click()
        WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,"//td[text()='车主信息']")))
        self.driver.find_element_by_xpath("//input[@name='txtOwnName']").send_keys(txtOwnName)
        self.driver.find_element_by_xpath("//input[@name='txtIDCardNumber']").send_keys(txtIDCardNumber)
        self.driver.find_element_by_xpath("//input[@name='txtOwnTel']").send_keys(txtOwnTel)
        self.driver.find_element_by_xpath("//input[@name='txtVIN']").send_keys(txtVIN)
        self.driver.find_element_by_xpath("//input[@name='txtBrand']").send_keys(txtBrand)
        self.driver.find_element_by_xpath("//input[@name='txtMotorNumber']").send_keys(txtMotorNumber)
        self.driver.find_element_by_xpath("//input[@name='txtColor']").send_keys(txtColor)
        self.driver.find_element_by_xpath("//input[@name='btnSave']").click()

    #删除信息
    def Del_data(self):
        WebDriverWait(self.driver, 20).until(ec.frame_to_be_available_and_switch_to_it("251"))
        WebDriverWait(self.driver, 20).until(ec.frame_to_be_available_and_switch_to_it("bicycleregifr"))
        WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,"//input[@title='删除']")))
        self.driver.find_element_by_xpath("//input[@title='删除']").click()
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[text()='提示']")))
        self.driver.find_element_by_xpath("// button[text() = '确定']").click()
        # // button[text() = '取消']
        # // div[text() = '提示'] / following - sibling::a


    #登记成功元素获取
    def SuccessfulRegistration(self):
        WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,"//div[text()='添加成功!']")))
        tex = self.driver.find_element_by_xpath("//div[text()='添加成功!']").text
        return tex

    #为空数据元素获取
    def ErrorRegistration(self):
        WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,"//div[@id='massage']")))
        return self.driver.find_element_by_xpath("//div[@id='massage']").text

    #验证删除数据
    def Number_elements(self):
        WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,"//td[text()='当前没有车辆信息']")))

        ele = self.driver.find_element_by_xpath("//td[text()='当前没有车辆信息']").text
        return ele