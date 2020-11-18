'''
1,接口性能测试，比较某个接口在500ms返回
2、耗时比较久的操作，默认的超时时间执行不完，比如上传超大的文件，可以设置大一点的超时时间
'''
import requests

url = 'https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel = 15091714854'
# 0.1 表示100ms
# for i in range(10):
#     try:
#         r = requests.get(url,timeout=0.1)
#         print(r.status_code)
#     except Exception as e:
#         print(e)

'''
proxies 代理
1. 通过代理抓包，用fiddler抓自动化发的报文分析，定位问题
2. 服务器把IP封掉了，可以通过代理换个Ip访问
'''

proxy = {
    "http":"http://127.0.0.1:8888", #http代理
    "https": "http://127.0.0.1:8888" # https代理
}
# 设置proxies时，需要打开代理服务器，比如Fiddler
r = requests.get("http://www.baidu.com", proxies=proxy)
print(r.text)
# 不加
r = requests.get("https://www.bagevent.com",proxies=proxy, verify = False)
print(r.text)

