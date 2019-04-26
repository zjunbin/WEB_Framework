#  coding utf-8
# @time      :2019/4/2410:39
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :LogPage_Locator.py
from selenium.webdriver.common.by import By


class LoginPageLocator:
    # 用户名元素
    user_name = (By.XPATH, "//*[@name='txtName']")
    # 密码元素
    user_pwd = (By.XPATH, "//*[@name='txtPass']")
    # 验证码元素
    user_code = (By.XPATH, "//*[@name='txt_code']")
    # 登录按钮元素
    user_button = (By.XPATH, "//*[@name='loginBtn']")
    # 登录成功页面验证
    log_page = (By.XPATH, "//*[@class='aui_content']")
    #页面检查元素
    page_check  =(By.XPATH,"//span[ @id = 'lblTips']")

    print(user_name)