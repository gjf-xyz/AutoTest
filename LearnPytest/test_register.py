import requests


def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    response = requests.post(url, data=data)
    return response



# 手机号码格式不正确
def test_register_001():
    # 测试数据
    data = {"mobilephone": 1383838383, "pwd": 123456, "regnam": "aaa"}
    # 期望结果
    expected = {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}
    # 测试步骤
    real = register(data)
    # 检查结果
    assert real.json()['msg'] == expected['msg']
    assert real.json()['code'] == expected['code']

# 密码格式错误
def test_register_002():
    # 测试数据
    data = {"mobilephone": 13838383838, "pwd": 12345, "regnam": "aaa"}
    # 期望结果
    expected = {"status":0,"code":"20108","data": None,"msg":"密码长度必须为6~18"}
    # 测试步骤
    real = register(data)
    # 检查结果
    assert real.json()['msg'] == expected['msg']
    assert real.json()['code'] == expected['code']

# 注册成功
def test_register_003():
    data = {"mobilephone": "", "pwd": "", "regnam": "aaa"}
    expected = {"status": "", "code": "", "data": None, "msg": "参数错误：参数不能为空"}
    real = real = register(data)
    assert real.json()['msg'] == expected['msg']
    assert real.json()['code'] == expected['code']

def test_register_004():
    # 测试数据
    data = {"mobilephone": 13312345678, "pwd": 123456, "regnam": "aaa"}
    # 期望结果
    expected = {"status": 1, "code": "10001", "data": None, "msg": "注册成功"}
    # 测试步骤
    real = register(data)
    # 检查结果
    assert real.json()['msg'] == expected['msg']
    assert real.json()['code'] == expected['code']