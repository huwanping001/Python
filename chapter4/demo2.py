# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/18 9:54

#测试对象的bool值

print(bool(False)) #False
print(bool(0)) #False
print(bool(0.0)) #False
print(bool(None)) #False
print(bool('')) #False
print(bool("")) #False

print(bool(list())) #空列表 False
print(bool([])) #空列表 False

print(bool(())) #空元组 False
print(bool(tuple())) #空元组 False

print(bool({})) #空字典 False
print(bool(dict())) #空字典False

print(bool(set())) #空集合 False


print('-----------------其他对象的bool值均为True------------------')
print(bool(18))
print(bool(True))
print(bool('xiaohu'))