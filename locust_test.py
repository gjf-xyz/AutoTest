'''
性能测试
'''
from locust import HttpUser, between, task

'''
1.为要模拟的用户定义一个类，从HttpUser继承
'''


class CarRental(HttpUser):
    # between 是User类中定义的一个方法
    # wait_time 是User类定义的一个属性，表示等待时间
    wait_time = between(3, 8)  # 任务跟任务之间的等待时间在3~8之间取随机数

    @task
    def loadAllRent(self):
        #
        self.client.get("/carRental/rent/loadAllRent.action?page=1&limit=10")

    @task
    def loadAllMenu(self):
        self.client.get("/carRental/menu/loadAllMenu.action?page=1&limit=10")

# -f 要执行的文件
# --web-host locust web
# --web-port locust web
# locust -f locust_test.py --host=http://127.0.0.1:8080
# locust -f locust_test.py --step-load
