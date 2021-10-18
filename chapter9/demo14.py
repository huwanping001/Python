# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/28 16:51

'''
·编码与解码的方式
·编码：将字符串转换为二进制数据（bytes）
·解码：将bytes类型的数据转换成字符串类型
'''

#编码
s = '天涯共此时'
print(s.encode(encoding='GBK')) #在GBK这种编码格式中，一个中文占两个字节
print(s.encode(encoding='UTF-8')) #在UTF-8这种编码格式中，一个中文占3个字节

#解码
#byte代表的就是一个二进制数据（字节类型的数据）
byte=s.encode(encoding='GBK') #编码
print(byte.decode(encoding='GBK')) #解码

byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))

