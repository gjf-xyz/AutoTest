"""
上传文件:一般都是post接口，用files参数上传文件
"""
import requests

url = "http://www.httpbin.org/post"

'''
fiels参数，字典的格式，'name':file-tuple
file-tuple可以是2-tuple('filename', fileobj)、3-tuple('filename', fileobj, 'content_type')、
4-tuple('filename', fileobj, 'content_type', custom_headers)
'''
with open("d:/test.txt", encoding="utf-8") as f:
    #
    file = {"file1": ("test.txt", f, "text/plain")}  # MIME类型：text/plain、image/png、image/gif
    r = requests.post(url, files=file)
    print(r.text)
    # \ufeff\u4e2d\u6587\u5b57 unicode编码的

with open("d:/p.jpg","rb") as f:
    file = {"file2": ("pic.jpeg", f, "image/jpg")}
    r = requests.post(url, files=file)
    print(r.text)

# 可以一次上传多个文件
with open("d:/test.txt", encoding="utf-8",) as f1:
    # file1 = {"file1": ("test.txt", f1, "text/plain")}  # MIME类型：text/plain、image/png、image/gif
    with open("d:/p.jpg","rb") as f2:
        file2 = {"file1": ("test.txt", f1, "text/plain"),"file2": ("pic.jpeg", f2, "image/jpg")}
        r = requests.post(url,files=file2)
        print(r.text)
