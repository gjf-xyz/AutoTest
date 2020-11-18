"""
任务集合：分层的方式，按模块
"""
from locust import TaskSet, task, HttpUser, between


# 租车系统
# 系统管理模块

class SystemManager(TaskSet):
    @task
    def task1(self):
        self.client.get('/carRental/sys/toUserManager.action')

    @task
    def task2(self):
        self.client.get('/carRental/sys/toRoleManager.action')

    @task
    def task3(self):
        self.client.get('/carRental/sys/toLogInfoManager.action')


# 基础管理模块
class BasicManager(TaskSet):
    @task(7)  # 括号中的数字表示权重，默认是1
    def task1(self):
        self.client.get('/carRental/bus/toCustomerManager.action')

    @task(3)
    def task2(self):
        self.client.get('/carRental/bus/toCarManager.action')


class CarRentalTest(HttpUser):
    wait_time = between(1, 3)  # 任务之间的间隔时间
    # tasks = [BasicManager, SystemManager]  # 任务集合，tasks是user中定义的属性，不能写错
    tasks = {BasicManager: 4, SystemManager: 1}

    # htt}p://127.0.0.1:8089/carRental/sys/toUserManager.action

    def on_start(self):  # 测试前置
        user = {"loginname": "admin", "pwd": "123456"}
        self.client.post("/carRental/login/login.action", data=user)

    def on_stop(self):  # 测试后置，退出登录，在结束运行时每个用户调用一次
        self.client.post("/carRental/login/login.action")  # 乱写的接口，执行时失败
