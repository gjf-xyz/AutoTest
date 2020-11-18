'''
注册的测试脚本（pytest）
'''
import pytest

from ZongHe.caw import DataRead
from ZongHe.baw import Member, DbOp
from ZongHe.caw.BaseRequests import BaseRequests
from ZongHe.test_script.conftest import db


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_fail.yaml"))
def fail_data(request):  # 固定写法
    return request.param


# 注册失败
def test_register_fail(fail_data, url, baserequests):
    print(f"测试数据为：{fail_data['casedata']}")
    print(f"预期结果为：{fail_data['expect']}")

    # 发送请求
    r = Member.register(url, baserequests, fail_data["casedata"])
    print(r)
    # 1.检查响应的结果
    assert r.json()["status"] == fail_data["expect"]["status"]
    assert r.json()["code"] == fail_data["expect"]['code']


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_pass.yaml"))
def pass_data(request):
    return request.param


# 注册成功
def test_register_pass(pass_data, url, db, baserequests):
    print(f"测试数据为：{pass_data['casedata']}")
    print(f"预期结果为：{pass_data['expect']}")
    phone = pass_data['casedata']['mobilephone']
    # 初始化环境，确保环境中没有
    DbOp.deleteUser(db, phone)
    # 发送请求
    r = Member.register(url, baserequests, pass_data["casedata"])
    print(r.json())
    # 检查结果
    assert r.json()["status"] == pass_data["expect"]["status"]
    assert r.json()["code"] == pass_data["expect"]["code"]
    # 2. 检查实际有没有注册成功（1、查数据库 2、获取用户列表 3、用注册的用户列表
    r = Member.getlist(url,baserequests)
    print(r.text)
    assert phone in r.text
    #  清理环境，根据手机号删除注册用户
    DbOp.deleteUser(db, phone)


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_repeat.yaml"))
def repeat_data(request):
    return request.param


# 重复注册
def test_register_repeat(repeat_data, url, baserequests):
    print(f"测试数据为：{repeat_data['casedata']}")
    print(f"预期结果为：{repeat_data['expect']}")
    phone = repeat_data['casedata']['mobilephone']
    # 环境初始化
    DbOp.deleteUser(db,phone)
    # 发送请求
    r=Member.register(url, baserequests, repeat_data["casedata"])
    # 检查结果
    assert r.json()["status"] == pass_data["expect"]["status"]
    assert r.json()["code"] == pass_data["expect"]["code"]
    # 2. 检查实际有没有注册成功（1、查数据库 2、获取用户列表 3、用注册的用户列表
    r = Member.getlist(url, baserequests)
    print(r.text)
    assert phone in r.text
    r = Member.register(url, baserequests, repeat_data["casedata"])
    # 检查结果
    assert r.json()["status"] == repeat_data["expect"]["status"]
    assert r.json()["code"] == repeat_data["expect"]["code"]
    # 清理环境
    DbOp.deleteUser(db,phone)



