# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/22 17:07

'''元组的遍历'''
'''第一种获取元组元素的方式，使用索引'''
t = ('Python', 'world', 98)
print(t[0])
print(t[1])
print(t[2])
#print(t[3]) #IndexError: tuple index out of range

'''遍历元组'''
for item in t:
    print(item)
