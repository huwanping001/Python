# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/10/6 11:13

#封装  两个下划线__
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def show(self):
        print(self.name, self.__age)

stu = Student('张三', 20)
stu.show()

#在类外使用name与age
print(stu.name)
#print(stu.__age)  #AttributeError: 'Student' object has no attribute '__age'

#print(dir(stu))
print(stu._Student__age)  #在类的外部可以通过  _Student__age 进行访问