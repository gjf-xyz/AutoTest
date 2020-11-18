'''
发送post请求
'''
import requests
# 发送post请求，带参数时，可以使用data或josn来传参，具体使用哪个要看系统怎么实现的
# 上一步注册成功的手机号，验证登录，登录使用post
# 带请求头使用headers

url = "http://jy001:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone":"15091109871","pwd":"123456Sd"}
r = requests.post(url,data=canshu) # 表单
print(r.text)

r = requests.post(url,json = canshu) # json，金融系统不支持json方式传参
print(r.text)
# 发送请求到httpbin,观察区别
r = requests.post("http://www.httpbin.org/post",json=canshu) #"Content-Type"："application/x-www-form-urlencoded"
print(r.text)
r = requests.post("http://www.httpbin.org/post",json=canshu) # "Content-type":"application/json"
print(r.text)