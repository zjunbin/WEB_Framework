#  coding utf-8
# @time      :2019/4/2614:31
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :basepage.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from WEB_Framework.common.do_mylog import MyLog
from WEB_Framework.common import globpath
import datetime,time


# mylog = MyLog()

class BasePage:

    def __init__(self,driver):
        self.driver = driver


    #等待元素可见
    def wait_element_Visible(self, locator, timeout = 30, poll_frequency= 0.5, model_name=None):
        # mylog.info('等待{}元素可见'.format(locator))
        try:
            #获取开始时间
            starttime = datetime.datetime.now()
            # 等待元素
            WebDriverWait(self.driver, timeout, poll_frequency).until(ec.visibility_of_element_located(locator))
            #获取结束的时间
            endtime = datetime.datetime.now()
            #获取等待时长
            # mylog.info('等待元素总时长{}'.format((endtime - starttime).seconds))
        except Exception as e:
            #写日志
            # mylog.error(e)
            self.save_iamge(model_name)
            raise



    def get_element(self,model_name ,locator):
        # mylog.info('查找模块{}下的元素：{}'.format(model_name, locator))
        try:
            ele = self.driver.find_element(*locator)
            return ele
        except:
            # mylog.error('查找模块{}下的元素：{}。失败'.format(model_name, locator))
            raise

    def click_element(self,model_name ,locator):
        # 查找元素
        ele = self.get_element(model_name ,locator)
        # 元素操作
        # mylog.info('点击操作：{}下的元素：{}'.format(model_name, locator))
        try:
            ele.click()
        except:
            raise


    def input_text(self,model_name ,locator ,value):
        # 查找元素
        ele = self.get_element(model_name,locator)
        # 元素操作
        # mylog.info('输入操作：{}下的元素{}'.format(model_name, locator))
        try:
            ele.send_keys(value)
        except:
            raise

    def get_element_attribute(self,model_name ,locator ,attr):
        # 查找元素
        ele = self.get_element(model_name, *locator)
        # 元素操
        # mylog.info('获取元素属性：{}下的元素{}的属性{}'.format(model_name, locator ,attr))
        try:
            return ele.get_attribute(attr)
        except:
            # mylog.error('获取元素属性失败：{}下的元素{}的属性{}'.format(model_name, locator ,attr))
            self.save_iamge(model_name)
            raise

    def get_element_text(self, model_name ,locator):
        ele = self.get_element(model_name ,*locator)
        # mylog.info('获取元素文本值：模块{} 下 {}的文本值'.format(model_name,locator))
        try:
            return ele.text
        except:
            # mylog.info('获取元素文本值失败：模块{} 下 {}的文本值'.format(model_name, locator))
            raise

    def save_iamge(self,model_name):

        # 文件名称  当前时间
        filepath = globpath.screenshot_path + '{}_{}.png'.format(model_name,time.strftime("%Y-%m-%d %H-%M-%S",time.localtime()))
        try:
            self.driver.save_screenshot(filepath)
            # mylog.info("截图成功，文件路径为:{}".format(filepath))
        except Exception as e:
            # mylog.error("截屏保存失败")
            raise e

    def switch_window(self):
        pass

    def switch_alter(self):
        pass

    def upload(self):
        pass