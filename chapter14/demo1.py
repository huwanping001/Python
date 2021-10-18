# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/10/7 20:20

def fun1():
    pass
def fun2():
    pass

class Student:
    native_place = '四川' #类属性
    def eat(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def cm(cls):
        pass
    @staticmethod
    def sm():
        pass

a = 10
b = 20
print(a+b)