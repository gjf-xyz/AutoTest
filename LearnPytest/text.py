import requests


def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/reqister"
    response = requests.post(url, data=data)
    return response


# 手机号码格式不正确
def test_register_001():
    # 测试数据
    data = {"mobilephone": 1771234567, "pwd": 123456, "reqnam": "aaa"}
    # 期望结果
    expected = {"ststus": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}
    # 测试步骤
    real = register(data)
    # 检查结果
    assert real.json()['msg'] == expected['msg']
    assert real.json()['code'] == expected['code']


# 密码格式错误
def test_register_002():
    # 测试数据
    data = {"mobilephone": 1551234567, "pwd": 1234, "reqname": "bbb"}
    # 期望结果
    expected = {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}
    # 测试步骤
    real = register(data)
    # 检查结果
    assert real.json()['msg'] == expected['msg']
    assert real.json()['code'] == expected['code']
