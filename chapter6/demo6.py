# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/22 10:25

#向列表的末尾添加一个元素
'''	list.append(obj)
在列表末尾添加新的对象'''
lst = [1, 2, 3]
print('添加元素之前：', lst, id(lst))
lst.append(4)
print('添加元素后：', lst, id(lst))
lst2 = ['xiaohu', 'tongxue']
lst.append(lst2) #将lst2作为一个元素添加到列表的末尾
print(lst)

'''	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）'''

lst.extend(lst2)
print(lst)

'''list.insert(index, obj)
将对象插入列表'''
lst.insert(1, 20)
print(lst)

#切片添加
lst3 = [True, False, 'hello']
#在任意的位置上添加N多个元素
lst[1:] = lst3
print(lst)


