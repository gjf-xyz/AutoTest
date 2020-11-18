'''
监控代码：监控服务器的内存、cpu、网络、磁盘等。
'''
from datetime import time, datetime

import psutil

print(psutil.cpu_percent()) #获取cpu信息
print(psutil.virtual_memory()) # 虚拟内存
print(psutil.virtual_memory().percent) #虚拟内存百分比
print(psutil.disk_usage("d:/")) # 租车系统所在的磁盘百分比
print(psutil.disk_usage("d:/").percent)

print(psutil.net_io_counters().bytes_sent) #发y送的字节数
print(psutil.net_io_counters().bytes_recv) # 接收的字节数


# 达到类似serveragent的效果，在性能测试期间，获取cpu、内存的趋势
# 死循环，每隔3s读一次，把读的结果写到文件中，测试结束后分析文件，使用excel等生成图表
# 时间戳 cpu% 内存% 磁盘% 发送字节数 接收字节数"
with open("d:/资源占用情况.txt",encoding='utf-8',mode='a') as file:
    file.write("时间戳\tCPU%\t内存%\t磁盘%\t发送字节数\t接收字节数")
    while True:
        print("监控中............")
        file.write(datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%s")+"\t")
        file.write(str(psutil.cpu_percent())+ "%\t")
        file.write(str(psutil.virtual_memory().percent)+ "%\t")
        file.write(str(psutil.disk_usage("d:/").percent) + "%\t")
        file.write(str(psutil.net_io_counters().bytes_sent) + "\t")
        file.write(str(psutil.net_io_counters().bytes_recv) + "\n")
        file.flush() #从缓存刷新到文件中，避免文件没关闭，之前的内容一直写不进去
        time.sleep(3)



