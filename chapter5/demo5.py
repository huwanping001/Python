# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/18 15:49

#for in循环 可迭代对象

for i in 'python':  #第一取出来的是p，将p赋值给i，将i值输出
    print(i)

#range() 产生一个整数序列，也是一个可迭代对象
for i in range(10):
    print(i)

#如果在循环体中不需要使用到自定义变量，可将自定义变量写为“_”
for _ in range(5):
    print('xiaohu')

#for循环计算1-100之间的偶数和
sum = 0
for i in range(2, 102, 2):
    sum += i
print(sum)

#另一种写法
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print('1-100之间的偶数和为：', sum)