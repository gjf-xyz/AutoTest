'''
登录的测试脚本
'''
import pytest

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_fail.yaml"))
def fail_data(request):
    return request.param


@pytest.fixture(params=DataRead.readyaml("ZongHe\data_case\login_pass.yaml"))
def pass_data(request):
    return request.param

#测试的前置和后置
@pytest.fixture()
def register(url,baserequests,db):
    # 注册
    phone = test_register_pass()['casedata']['mobilephone']
    DbOp.deleteUser(db,phone)
    Member.register(url,baserequests,test_register_pass['casedata'])
    # 删除注册用户
    DbOp.deleteUser(db,phone)







# 注册成功
def test_register_pass(pass_data, url, db, baserequests):
    print(f"测试数据为：{pass_data['casedata']}")
    print(f"预期结果为：{pass_data['expect']}")
    # 发送请求
    r = Member.register(url, baserequests, pass_data["casedata"])
    print(r.json())
    # 检查结果
    assert r.json()["status"] == pass_data["expect"]["status"]
    assert r.json()["code"] == pass_data["expect"]["code"]


# 登录失败
def test_login_fial(fail_data, url, baserequests):
    print(f"测试数据为：{fail_data['casedata']}")
    print(f"预期结果为：{fail_data['expect']}")

    # 发送请求
    r = Member.login(url, baserequests, fail_data["casedata"])
    print(r)
    # 检查结果
    assert r.json()["status"] == fail_data["expect"]["status"]
    assert r.json()["code"] == fail_data["expect"]['code']


# 登录成功
def test_login(pass_data, url, baserequests):
    print(f"测试数据为：{pass_data['casedata']}")
    print(f"预期结果为：{pass_data['expect']}")
    phone = pass_data['casedata']['mobilephone']

    # 发送请求
    r = Member.login(url, baserequests, pass_data["casedata"])
    print(r)
    # 检查结果
    assert r.json()["status"] == pass_data["expect"]["status"]
    assert r.json()["code"] == pass_data["expect"]['code']
