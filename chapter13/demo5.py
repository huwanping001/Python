# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/10/6 16:47

#方法重写

'''•如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其（方法体）进行重新编写
·子类重写后的方法中可以通过super()xxx() 调用父类中被重写的方法'''

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

    def info(self):  #方法重写
        super().info()
        print(self.stu_no)

class Teacher(Person):
    def __init__(self, name, age, teacheryear):
        super().__init__(name, age)
        self.teacheryear = teacheryear

    def info(self):
        super().info()
        print(self.teacheryear)


stu = Student('小胡', '20', '1001')
teacher = Teacher('李四', '35', '8')

stu.info()
print('-------------------')
teacher.info()

