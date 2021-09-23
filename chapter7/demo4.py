# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/22 15:29

score = {'xiaohu': 98, 'xiaolan': 100, 'xiaobai': 99}
'''获取所有的key'''
keys = score.keys()
print(keys)
print(type(keys))
print(list(keys)) #将所有的key组成的视图转成列表

#获取所有的value
values = score.values()
print(values)
print(type(values))
print(list(values))

#获取所有的键值对
items = score.items()
print(items)
print(list(items)) #转换之后的列表元素是由元组组成的