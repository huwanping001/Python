# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/28 16:34

'''格式化字符串的第一种方式 % 作占位符'''

name = '张三'
age = 20
print('我叫%s，今年%d岁' % (name, age))

'''2{}'''
print('我叫{0}，今年{1}岁'.format(name,age))

'''3f-string'''
print(f'我叫{name}，今年{age}岁')

