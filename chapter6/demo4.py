# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/22 9:54

lst = ['xiaohu', 'black', 'white', 'yellow', 'blue', 99]
#获取索引为2和-4的元素
print(lst[2])
print(lst[-4])

#获取索引为10的元素
#print(lst[10]) #IndexError: list index out of range

#切片操作
lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
#start = 1, stop = 6, step = 1
#print(lst1[1:6:1])

print('原列表：', id(lst1))
lst2 = lst1[1:6:1]
print('切的片段：', id(lst2))

print(lst1[1:6])#默认步长为1

#start = 1, stop = 6, step = 2
print(lst1[1:6:2])

#start = 1, stop省略, step = 2
print(lst1[1::2])

#start 省略, stop = 6, step = 2
print(lst1[:6:2])


print('---------步长为负数的情况---------------')
print('原列表', lst1)
print(lst1[::-1])

#start = 7,stop省略 step = -1
print(lst1[7::-1])

#start = 1, stop = 6, step = 2
print(lst1[6:0:-2])