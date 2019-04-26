#  coding utf-8
# @time      :2019/4/2410:06
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :login_datas.py

# 登录成功用例
success_data={'username':"888888",'pwd':'123456','code':'123456'}

# 登录数据为空的测试用例
datacase=[
    {'username':"",'pwd':'123456','code':'123456','excepted':'账号不能为空!'},
    {'username': "adf955", 'pwd': '','code':'123456','excepted':'密码不能为空!'},
    {'username':"888888",'pwd':'123456','code':'','excepted':'验证码不能为空!'},
    {'username':"888888",'pwd':'123456','code':'adfgf','excepted':'验证码为数字，并且必须是5位'}
]
# 错误的测试用例
dataerror=[
    {'username':"888888",'pwd':'655444','code':'123456','excepted':'抱歉，账号或密码错误！'},
    {'username': "2222222", 'pwd': '123456','code':'123456','excepted':'抱歉，账号或密码错误！'},
    {'username':"888888",'pwd':'5466544','code':'123456','excepted':'抱歉，账号或密码错误！'}
]