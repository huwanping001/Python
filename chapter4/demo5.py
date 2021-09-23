# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/18 11:26
'''多分支结构，多选一执行，从键盘录入一个整数
90-100 A
80-89 B
70-79 C
60-69 D
0-59 E
小于0或大于100 为非法数据（不是成绩的有效范围）'''

score = int(input('请输入一个成绩'))
#判断
if score >= 90 and score <= 100: #这个'score >= 90 and score <='可以改为'90<=score<=100'
    print('A级')
elif score >= 80 and score <= 89:
    print('B级')
elif score >= 70 and score <= 79:
    print('C级')
elif score >= 60 and score <= 69:
    print('D级')
elif score >= 0 and score <= 59:
    print('E级')
else:
    print('对不起成绩有误，不在成绩的有效范围')