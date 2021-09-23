# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/18 14:34

#嵌套循环

'''会员 >= 200 8折
       >= 100 9折
       不打折
    非会员 >= 200 9.5折
        不打折'''

answer = input('你是会员吗？y/n')
money = float(input('请输入你的购物金额：'))
#外层判断是否为会员
if answer == 'y':   #会员
    if money >= 200:
        print('打八折，付款金额为：', money*0.8)
    elif money >= 100:
        print('打九折，付款金额为：', money*0.9)
    else:
        print('不打折，付款金额为：', money)
else: #非会员
    if money >= 200:
        print('打九折，付款金额为：', money*0.95)
    else:
        print('不打折，付款金额为：', money)