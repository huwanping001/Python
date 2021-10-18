# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/10/9 15:04

'''sys与Python解释器及其环境操作相关的标准库
time提供与时间相关的各种函数的标准库
os提供了访问操作系统服务功能的标准库
calendar提供与日期相关的各种函数的标准库
urllib用于读取来自网上（服务器）的数据标准库
json用于使用JSON序列化和反序列化对象
re用于在字符串中执行正则表达式匹配和替换
math提供标准算术运算函数的标准库
decimal用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算
logging 提供了灵活的记录事件、错误、警告和调试信息等目志信息的功能'''

import time
import urllib.request
import sys
import math

print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())
print(time.localtime(time.time()))

print(urllib.request.urlopen('http://www.baidu.com').read())

print(math.pi)