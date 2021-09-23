# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/22 11:16

lst = [20, 40, 10, 98, 54]
print('排序前的列表', list, id(lst))
#开始排序，调用列表对象的sort方法，升序排序
lst.sort()
print('排序后的列表', lst, id(lst))

#通过制定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True) #reverse=True 表示降序排序，#reverse=False 表示升序排序，
print(lst)

lst.sort(reverse=False) #reverse=True 表示降序排序，#reverse=False 表示升序排序，
print(lst)

print('---使用内置函数sorted()对列表进行排序，将产生一个新的列表对象---')
lst = [20, 40, 10, 98, 54]
print('原列表', lst)
#开始排序
new_lst = sorted(lst)
print(lst)
print(new_lst)

#指定关键字参数，实现列表元素的降序排序
desc_lst = sorted(lst,  reverse=True)
print(desc_lst)