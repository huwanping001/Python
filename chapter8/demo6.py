# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/23 14:31

#集合的相关操作
#判断
s = {10, 20, 30, 405, 60}
print(10 in s) #True
print(100 in s) #False
print(10 not in s) #False
print(100 not in s) #True

'''集合元素的新增操作'''
s.add(80) #一次添加一个元素
print(s)

s.update({200, 400, 300}) #一次至少添加一个元素
print(s)

s.update([100, 90, 70])
s.update((1, 2, 3))
print(s)

'''集合元素的删除操作'''
s.remove(100)
print(s)
#s.remove(500)#KeyError: 500

s.discard(500)
s.discard(300)
print(s)

s.pop()
print(s)
s.pop()
print(s)

#s.pop(200)  #TypeError: pop() takes no arguments (1 given)

s.clear()
print(s)