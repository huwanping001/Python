# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/22 10:39

'''list.remove(obj)
移除列表中某个值的第一个匹配项'''
lst = [10, 20, 30, 40, 50, 60, 30]
lst.remove(30) #从列表中移除一个元素，如果有重复元素只移第一个元素
print(lst)
#lst.remove(100) #ValueError: list.remove(x): x not in list

'''list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值'''
lst.pop(1)
print(lst)
#lst.pop(5) #IndexError: pop index out of range 指定的索引不存在，将抛出异常
lst.pop()
print(lst) #如果不指定参数，将默认删除列表中的最后一个元素

#切片  会产生新的列表对象

print('-------------切片操作--删除至少一个元素，将产生一个新的列表对象---------------------')
new_lst = lst[1:3]
print('原列表', lst)
print('切片后的列表', new_lst)

'''不产生新的列表对象，而是删除原列表的内容'''
lst[1:3]=[]
print(lst)

'''清楚列表中的所有元素'''
lst.clear()
print(lst)

'''del语句将列表对象删除'''
del lst
#print(lst) #NameError: name 'lst' is not defined


