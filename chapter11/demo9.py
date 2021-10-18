# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/29 19:17

'''
1 ZeroDivisionError 除（或取模）零 （所有数据类型）

2 IndexError 序列中没有此索引（index）

3 KeyError 映射中没有这个键

4 NameError 未声明/初始化对象 （没有属性）

5 SyntaxError Python 语法错误

6 ValueError 传入无效的参数'''

#1数学运算异常
#print(10/0) ZeroDivisionError: division by zero

#2
lst=[1,2,3]
#print(lst[4]) IndexError: list index out of range

#3
dic={'name':'张三','age':20}
#print(dic['gender']) KeyError: 'gender'

#4
#print(num) NameError: name 'num' is not defined

#5
#int a=20  SyntaxError: invalid syntax

#6
#a = int('hello') ValueError: invalid literal for int() with base 10: 'hello'
