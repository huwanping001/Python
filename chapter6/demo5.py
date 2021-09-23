# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/22 10:12

#列表元素的判断以及遍历
print('p' in 'python')  #True
print('k' not in 'python') #True

lst = [10, 20, 'xiaohu', 'tongxue']
print(10 in lst) #True
print(100 in lst) #False
print(10 not in lst) #False
print(100 not in lst) #True

for i in lst:
    print(i)