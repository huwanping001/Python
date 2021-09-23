# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/23 14:51

#集合的数学操作

#1交集
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print(s1.intersection(s2))
print(s1 & s2)  #intersection()与&等价，交集操作
print(s1)
print(s2)

#2并集操作
print(s1.union(s2))
print(s1 | s2)
print(s1)
print(s2)

#3差集操作
print(s1.difference(s2))
print(s1-s2)
print(s1)
print(s2)

#4对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2)

