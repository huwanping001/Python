# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/29 11:01

#递归函数

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(6))