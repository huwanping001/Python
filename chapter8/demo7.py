# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/23 14:42

'''两个集合是否相等（元素相同就相等）'''
s1 = {10, 20, 30, 40}
s2 = {30, 40, 20, 10}
print(s1 == s2) #True
print(s1 != s2) #False

'''一个集合是否是另一个集合的子集'''
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print(s2.issubset(s1)) #True
print(s3.issubset(s1)) #False

'''一个集合是否是另一个集合的超集'''
print(s1.issuperset(s2)) #True
print(s1.issuperset(s3)) #False

'''两个集合是否含有交集'''
print(s2.isdisjoint(s3)) #False---有交集为False

s4 = {100, 200, 300}
print(s2.isdisjoint(s4)) #True---没交集为True
