#  coding utf-8
# @time      :2019/4/2515:24
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :Registration_use_case.py

success_data = {"txtOwnName":"张无","txtIDCardNumber":"445323194006190657","txtOwnTel":"13288000002",
                "txtVIN":"3423","txtBrand":"艾玛","txtMotorNumber":"3422","txtColor":"白色","exp":"添加成功!"}


error_data = [{"txtOwnName":"","txtIDCardNumber":"130283196203233604","txtOwnTel":"13288000000",
                "txtVIN":"123","txtBrand":"艾玛","txtMotorNumber":"123","txtColor":"白色","exp":"车主姓名不能为空！"},
{"txtOwnName":"张三","txtIDCardNumber":"","txtOwnTel":"13288000000",
                "txtVIN":"123","txtBrand":"艾玛","txtMotorNumber":"123","txtColor":"白色","exp":"身份证号不能为空！"},
{"txtOwnName":"张三","txtIDCardNumber":"130283196203233604","txtOwnTel":"",
                "txtVIN":"123","txtBrand":"艾玛","txtMotorNumber":"123","txtColor":"白色","exp":"车主电话不能为空！"},
{"txtOwnName":"张三","txtIDCardNumber":"130283196203233604","txtOwnTel":"13288000000",
                "txtVIN":"","txtBrand":"艾玛","txtMotorNumber":"123","txtColor":"白色","exp":"车架号不能为空！"},
{"txtOwnName":"张三","txtIDCardNumber":"130283196203233604","txtOwnTel":"13288000000",
                "txtVIN":"123","txtBrand":"","txtMotorNumber":"123","txtColor":"白色","exp":"品牌不能为空！"},
{"txtOwnName":"张三","txtIDCardNumber":"130283196203233604","txtOwnTel":"13288000000",
                "txtVIN":"123","txtBrand":"艾玛","txtMotorNumber":"","txtColor":"白色","exp":"电机号不能为空！"},
{"txtOwnName":"张三","txtIDCardNumber":"130283196203233604","txtOwnTel":"13288000000",
                "txtVIN":"123","txtBrand":"艾玛","txtMotorNumber":"123","txtColor":"","exp":"车辆颜色主色不能为空！"}
]