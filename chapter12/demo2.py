# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/29 19:47

class Student: #Student为类的名称（类名）由一个或多个单词组成，每个单词首字母大写，其余小写
    native_place = '四川' #直接写在类里面的变量，称为类属性

    def __init__(self, name, age):
        self.name = name #self.name称为实体属性，进行了一个赋值操作，将局部变量的值赋给实体属性
        self.age = age

    #实例方法
    def eat(self):
        print('学生在吃饭...')

    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')



#在类之外定义的称为函数，在类之内定义的称为方法

def drink():
    print('喝水...')

