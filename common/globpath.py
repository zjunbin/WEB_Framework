#  coding utf-8
# @time      :2019/4/410:33
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :globpath.py
import os
import time
path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
conf_path = os.path.join(path,'config')
data_case = os.path.join(path,'datas','case.xlsx')
log_path = os.path.join(path,'logs')
case_path= os.path.join(path,'cases')
html_name = time.strftime('%Y%m%d',time.localtime(time.time())) + '_report.html'
result_path = os.path.join(path,'report','report.html')
screenshot_path = os.path.join(path,'output/screenshot')
if __name__ == '__main__':
    import datetime ,time
    s = datetime.datetime.now()
    time.sleep(3)
    e = datetime.datetime.now()
    c = (e - s).seconds
    print(c)