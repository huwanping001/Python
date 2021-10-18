# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/10/6 21:50

#print(dir(object))

#特殊属性 __dict__  获得类对象或实例对象所绑定的所有属性和方法的字典

class A:
    pass
class B:
    pass
class D(A):
    pass
class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age

#创建C类的对象
x = C('Jack', 20) #x是C类的一个实例对象
print(x.__dict__)  #实例对象的属性字典
print(C.__dict__)  #类方法的字典
print(x.__class__) #<class '__main__.C'> 输出了对象所属的类
print(C.__bases__)  #C类的父类类型的元素
print(C.__base__)  #和C离得最近的父类,类的基类

print(C.__mro__)  #类的层次结构
print(A.__subclasses__()) #A的子类 子类的列表