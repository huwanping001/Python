# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/18 16:57

'''流程控制语句break与continue在二重循环中的使用'''

for i in range(5): #代表外层循环需要执行5次
    for j in range(1, 11):
        if j % 2 == 0:
            break
        print(j)

for i in range(5): #代表外层循环需要执行5次
    for j in range(1, 11):
        if j % 2 == 0:
            continue
        print(j, end='\t')
    print()