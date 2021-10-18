# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/26 16:53

'''index()查找子串substr第一次出现的位置，如果查找的子串不存在时，则抛出ValueError
rindex()查找子串substr最后一次出现的位置，如果查找的子串不存在时，则抛出ValueError
find()查找子串substr第一次出现的位置，如果查找的子串不存在时，则返回-1
rfind() 查找子|substr最后一次出现的位置，如果查找的子串不存在时，则返回-1'''

#字符串的查询操作
s = 'hello,hello'
print(s.index('lo'))#3
print(s.find('lo'))#3
print(s.rindex('lo'))#9
print(s.rfind('lo'))#9

#print(s.index('k'))ValueError: substring not found
print(s.find('k'))
#print(s.rindex('k'))ValueError: substring not found
print(s.rfind('k'))

#建议使用find和rfind方法