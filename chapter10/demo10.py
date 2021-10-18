# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/29 18:27

def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

#斐波拉契数列第六位上的数字
print(fib(6))

print('--------------------------------------')
#输出前六位上的数字
for i in range(1, 7):
    print(fib(i))
