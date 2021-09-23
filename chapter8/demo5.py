# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/23 11:27

'''集合的创建方式
第一种创建方式 使用{}'''
s = {2, 3, 4, 5, 6, 6, 7} #集合中的元素不允许重复
print(s)

'''第二种创建方式 set()'''
s1 = set(range(6))
print(s1, type(s1))

s2 = set([1, 2, 3, 4, 4, 5])
print(s2, type(s2))

s3 = set((1, 2, 3, 4, 4, 5,65)) #集合中的元素是无序的
print(s3, type(s3))

s4 = set('python')
print(s4, type(s4))

s5 = set({2, 3, 4, 5, 6, 6, 7})
print(s5, type(s5))

#定义空集合
s6 = {}
print(type(s6))

s7 = set()
print(type(s7))