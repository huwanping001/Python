# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/18 16:07

'''要求从键盘区录入密码，最多录入三次，如果正确就结束循环'''

for i in range(3):
    pwd = input('请输入密码：')
    if pwd == '888888':
        print('密码正确')
        break
    else:
        print('密码不正确，请重新输入')
