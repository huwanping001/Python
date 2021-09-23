# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/22 9:47

#列表的查询操作
'''list.index(obj)
从列表中找出某个值第一个匹配项的索引位置'''

lst = ['xiaohu', 'tongxue', 99, 'xiaohu']
print(lst.index('xiaohu'))
#print(lst.index('python'))  #ValueError: 'python' is not in list
#print(lst.index('xiaohu', 1, 3))  #ValueError: 'xiaohu' is not in list

print(lst.index('xiaohu', 1, 4))