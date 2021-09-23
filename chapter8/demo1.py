# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/22 16:30

'''可变序列和不可变序列'''
'''可变序列 列表，字典'''

lst = [10, 20, 30]
print(id(lst))
lst.append(100)
print(id(lst))

'''不可变序列  字符串，元组'''
s = 'hello'
print(id(s))
s = s + 'world'
print(id(s))
print(s)
