#  coding utf-8
# @time      :2019/4/1015:19
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :do_mylog.py
from WEB_Framework.common.do_readconfig import ReadConfig
from WEB_Framework.common import globpath
import logging,time
class MyLog:

    def my_log(self,level,msg):
        conf = ReadConfig()
        my_logger = logging.Logger('my_logger')
        my_logger.setLevel(conf.get('testconfig','log_level'))
        log_path = globpath.log_path
        formatter = logging.Formatter(conf.get('testconfig','formatter'))
        filename = log_path + time.strftime('%Y%m%d',time.localtime(time.time()))
        fh = logging.FileHandler(filename,'a',encoding='utf-8')
        ch = logging.StreamHandler()
        fh.setLevel(conf.get('testconfig','fh_level'))
        ch.setLevel(conf.get('testconfig','ch_level'))
        fh.format(formatter)
        ch.formatter(formatter)
        my_logger.addHandler(fh)
        my_logger.addHandler(ch)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log('DEBUG', msg)

    def info(self, msg):
        self.my_log('INFO', msg)

    def warning(self, msg):
        self.my_log('WARNING', msg)

    def error(self, msg):
        self.my_log('ERROR', msg)

    def critical(self, msg):
        self.my_log('CRITICAL', msg)
