# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/18 14:46


'''从键盘录入两个整数，比较两个整数的大小'''

num_a = int(input('请输入第一个整数'))
num_b = int(input('请输入第二个整数'))
#比较大小
'''if num_a >= num_b:
    print(num_a, '大于等于', num_b)
else:
    print(num_a, '小于', num_b)'''


#条件表达式
print('使用条件表达式进行比较')
print(str(num_a) + '大于等于' + str(num_b) if num_a >= num_b else str(num_a) + '小于' + str(num_b))

