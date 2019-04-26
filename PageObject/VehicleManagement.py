#  coding utf-8
# @time      :2019/4/2416:05
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :VehicleManagement.py
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class vehicleManagement:

    def __init__(self,driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def Management(self):
        WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,"//img[@id='morefun']")))
        self.driver.find_element(By.XPATH,"//img[@id='morefun']").click()
        WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,"//div[@id='divMenu_Icon']//a[@rel='211']")))
        self.driver.find_element(By.XPATH,"//div[@id='divMenu_Icon']//a[@rel='211']").click()

    #车辆详情
    def VehicleDetails(self):
        WebDriverWait(self.driver,10).until(ec.visibility_of_all_elements_located((By.XPATH,"//td//input[@type='button' and @data-value='5' and @title='详情']")))
        self.driver.find_element_by_xpath("//td//input[@type='button' and @data-value='5' and @title='详情']").click()


    #车辆删除
    def VehicleRemoval(self):
        pass

    #车辆编辑
    def VehicleEditing(self):
        pass