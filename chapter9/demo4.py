# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/28 10:49

#字符串中大小写转换的方法
'''
upper() 把字符串中所有字符都转成大写字母
lower() 把字符串中所有字符都转成小写字母
swapcase()把字符串中所有大写字母转成小写字母，把所有小写字母都转成大写字母
capitalize() 把第一个字符转换为大写，把其个字符转换为小写
title() 把每个单词的第一个字符转换为大写 把每个单词的剩」字符转换为小写
'''

s = 'hello python'
a = s.upper() #转成大写之后，会产生新的字符串对象
print(a, id(a))
print(s, id(s))

print(s.lower(), id(s.lower())) #转换之后，会产生一个新的字符串对象
print(s, id(s))

print(s == s.lower())
print(s is s.lower())

s2 = 'hello PYTHON'
print(s2.swapcase())

print(s2.capitalize())
