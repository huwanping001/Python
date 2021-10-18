# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/10/6 10:34

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name+'在吃饭')

stu1 = Student('张三', 20)
stu2 = Student('李四', 25)
print(id(stu1))
print(id(stu2))

print('--------为stu2动态绑定性别属性------------')
stu2.gender = '女'
print(stu1.name, stu1.age)
print(stu2.name, stu2.age, stu2.gender)

print('--------------------')
stu1.eat()
stu2.eat()

def show():
    print('定义在类之外的称为函数')
stu1.show = show()  #动态绑定方法
stu1.show

