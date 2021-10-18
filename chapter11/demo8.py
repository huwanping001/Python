# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/29 19:15

try:
    a = int(input('请输入第一个整数:'))
    b = int(input('请输入第二个整数:'))
    result = a/b
except BaseException as e:
    print('出错了', e)
else:
    print(result)
finally:
    print('谢谢你的使用')
