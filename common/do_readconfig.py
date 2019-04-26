#  coding utf-8
# @time      :2019/4/410:31
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :do_readconfig.py
from common import globpath
import configparser
import os
class ReadConfig:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(filenames= os.path.join(globpath.conf_path,'global.conf'),encoding='utf-8')
        res = self.conf.getboolean('switch','on')
        if res == True:
            self.conf.read(filenames=os.path.join(globpath.conf_path,'online.conf'),encoding='utf-8')
        else:
            self.conf.read(filenames=os.path.join(globpath.conf_path, 'test.conf'), encoding='utf-8')

    def getinit(self,section,option):
        return  self.conf.getint(section=section, option=option)

    def getboolean(self,section,option):
        return self.conf.getboolean(section=section, option=option)

    def get(self,section,option):
        return self.conf.get(section=section, option=option)

    def getfloat(self,section,option):
        return self.conf.getfloat(section=section, option=option)

    def getdict(self,section,option):
        return eval(self.conf.get(section=section, option=option))

if __name__ == '__main__':
    conf = ReadConfig()
    print(conf.get('db','host'))