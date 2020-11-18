'''
发送get请求
'''

import requests

# 接口地址："http://www.baidu.com"
# 发送一个get请求,r是收到的响应
r = requests.get("http://www.baidu.com")
r.encoding = "utf-8"
# 文本格式的响应内容
print(r.text)
# 响应码
print(r.status_code)
assert r.status_code == 200
# Ok
print(r.reason)
assert r.reason == 'OK'
# 获取用户列表
# http://jy001:8081/futureloan/mvc/api/member/list
m = requests.get("http://jy001:8081/futureloan/mvc/api/member/list")
print(m.text)
assert m.status_code == 200
assert m.reason == 'OK' and m.json()['status'] == 1
assert m.json()['code'] == '10001'
# get请求带参数
# 方法1： 拼接到URl后面（金融项目注册接口）
m1 = requests.get("http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=15091109871&pwd=123456Sd&regname=abcde")
print(m1.text)
assert m1.status_code == 200
assert m1.reason == 'OK'
# 方法2： 使用params 传参数
m1 = requests.get("http://jy001:8081/futureloan/mvc/api/member/register")
canshu = {"mobilephone":"","pwd":"123456","regname":""}
m1 = requests.get("http://jy001:8081/futureloan/mvc/api/member/register",params= canshu)
print(m1.text)

# get请求带请求头,User-Agent伪装成浏览器发送的请求，避免服务器屏蔽自动化发的请求
url = "http://www.httpbin.org/get" #一个测试网站，get是接口名字，发送的请求，原封的返回回来
m1 = requests.get(url)
print(m1.text)
# User-Agent 包含浏览器的版本号，操作系统的版本号等信息
tou = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
m1 = requests.get(url,headers=tou)
print(r.text)

url = "https://wenku.baidu.com/view/027d607deff9aef8941e06c0.html"
r = requests.get(url,headers=tou)
print(r.text)
print("蜂群算法源代码"in r.text)






