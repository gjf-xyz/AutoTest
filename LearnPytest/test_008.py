'''
取现接口
'''

from unittest import mock

import requests


class JingRong:
    # 充值接口方法
    def chongzhi(self, data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/recharge", data=data).json()
        return r
    # 取现接口方法
    def quxian(self, data):
        s = requests.post("http://jy001:8081/futureloan/mvc/api/member//withdraw", data=data).json()
        return s


class TestJingRong:
    def test_quxian(self):
        jingrong = JingRong()
        c = {"mobilephone": 18012345677, "amount": 1000}
        r = jingrong.chongzhi(c)
        assert r['msg'] == "充值成功"
        assert r['status'] == 1
        assert r['code'] == '10001'
        print(r)

        jingrong.quxian = mock.Mock(return_value={"status": 1, "code": '10001', "data": None, "msg": "取现成功"})
        # 调用取现接口
        data = {"mobilephone": 18012345677, "amount": 100}
        s = jingrong.quxian(data)
        assert s['msg'] == "取现成功"
        assert s['status'] == 1
        assert s['code'] == '10001'
        print(s)
