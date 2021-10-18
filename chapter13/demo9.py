# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/10/7 14:23

'''add () 通过重写 add ()方法，可使用自定义对象具有“+”功能
通过重写 len ()方法，让内置函数len()的参数可以是白定义类型
'''


a = 20
b = 100
c =a + b #两个整数类型的对象的相加操作
d = a.__add__(b)

print(c)
print(d)

class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name
    def __len__(self):
        return len(self.name)

stu1 = Student('Jack')
stu2 = Student('李四')

s = stu1 + stu2  #实现了两个对象的加法运算（因为在Student类中编写__add__()特殊的方法）
print(s)
s = stu1.__add__(stu2)
print(s)



print('---------------------------')
lst = [1, 2, 3, 4]
print(len(lst)) #len是内容函数len
print(lst.__len__())
print(len(stu1))