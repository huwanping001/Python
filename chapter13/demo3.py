# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/10/6 11:24

#继的实现

'''
· 如果一个类没有继承任何类，则默认继承object
• Python 支持多继承
• 定义子类时，必须在其构造函数中调用父类的构造函数
'''

class Person(object):  #Person默认继承object类
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

class Teacher(Person):
    def __init__(self, name, age, teacheryear):
        super().__init__(name, age)
        self.teacheryear = teacheryear


stu = Student('小胡', '20', '1001')
teacher = Teacher('李四', '35', '8')

stu.info()
teacher.info()



