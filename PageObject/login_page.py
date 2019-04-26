#  coding utf-8
# @time      :2019/4/2316:14
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from WEB_Framework.PageLocator.LogPage_Locator import LoginPageLocator  as loc
from WEB_Framework.common.basepage import BasePage

import time

class LoginPage(BasePage):
    # # # 用户名
    # user_name =(By.XPATH,"//*[@name='txtName']")
    # # 密码
    # user_pwd = (By.XPATH,"//*[@name='txtPass']")
    # # 验证码
    # user_code = (By.XPATH,"//*[@name='txt_code']")
    # # 登录按钮
    # user_button = (By.XPATH,"//*[@name='loginBtn']")


    # def __init__(self,driver):
    #     self.driver = driver


    def Login(self,username,password,code):
        self.wait_element_Visible(loc.user_name,model_name='登录页面输入框')
        # WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc.user_name))
        time.sleep(0.5)
        # self.driver.find_element(*loc.user_name).send_keys(username)
        # self.driver.find_element(*loc.user_pwd).send_keys(password)
        # self.driver.find_element(*loc.user_code).send_keys(code)
        # self.driver.find_element(*loc.user_button).click()
        self.input_text(model_name='登录页面的用户名输入框',locator = loc.user_name,value=username)
        self.input_text(model_name='登录页面的密码输入框',locator = loc.user_pwd,value=password)
        self.input_text(model_name='登录页面的验证码输入框',locator=loc.user_code,value=code)
        self.click_element(model_name='登录页面的提交按钮',locator=loc.user_button)


    def get_find_from_loginArea(self):
        # WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(loc.log_page))
        self.wait_element_Visible(loc.log_page,model_name='首页图片')
        # return self.driver.find_element(*loc.log_page).text
        return self.get_element_text('登录页面提示信息',loc.log_page)

    def get_error(self):
        # WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((loc.page_check)))
        self.wait_element_Visible(locator=loc.page_check,model_name='登录页面错误提示')
        # return self.driver.find_element(*loc.page_check).text
        return self.get_element_text(model_name='登录页面错误提示',locator=loc.page_check)