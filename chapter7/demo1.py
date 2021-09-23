# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/22 15:03
'''字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：

d = {key1 : value1, key2 : value2, key3 : value3 }


键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变的，如字符串，数字。

一个简单的字典实例：

dict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}'''


'''字典的创建方式，使用{}创建字典'''
score = {'xiaohu': 98, 'xiaolan': 100, 'xiaobai': 99}
print(score)
print(type(score))

'''第二种创建方式dict()'''
student = dict(name = 'jack', age = 20)
print(student)

'''创建空字典'''
d = {}
print(d)