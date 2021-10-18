# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/29 19:07

'''python异常处理机制'''
try:
    a = int(input('请输入第一个整数:'))
    b = int(input('请输入第二个整数:'))
    print(a / b)
except ZeroDivisionError:
    print('对不起，除数不能为0')
except ValueError:
    print('只能输入数字串')
print('程序结束')