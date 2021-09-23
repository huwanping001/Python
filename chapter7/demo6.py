# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/22 16:08

#1字典中所有元素都是一个key-value，key不允许重复，value可以重复
d = {'name':'张三', 'name':'李四'} #key不允许重复
print(d)

d = {'name':'张三', 'nikename':'张三'} #value可以重复
print(d)

#2字典中的元素是无序的根据key计算，而列表元素有序
lst = [10, 20, 30]
lst.insert(1, 100)
print(lst)

#d = {lst:100} #TypeError: unhashable type: 'list'
#print(d)


