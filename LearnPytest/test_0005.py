import pytest
import requests


def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data)
    return r


@pytest.fixture(params=[{"data": {"mobilephone": "12345678912", "pwd": "12345"},
                         "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
                        {"data": {"mobilephone": "1371234111a", "pwd": "123456abc", "regname": "aaa"},
                         "expect": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}},
                        {"data": {"mobilephone": "12345678913", "pwd": "123456789qwertyuiop"},
                        "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}}])
def a(request):
    return request.param


def test_zhuce(a):
    real = register(a["data"])
    assert real.json()["status"] == a["expect"]["status"]
    assert real.json()["msg"] == a["expect"]["msg"]
