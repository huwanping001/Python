# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/18 15:44

#计算1-100之间的偶数和

sum = 0
a = 1
while a <= 100:
    if a % 2 == 0: #if a%2
        sum += a
        a += 1
    else:
        a += 1
print(sum)

#另一种写法

sum = 0
a = 2
while a <= 100:
    sum += a
    a += 2
print(sum)