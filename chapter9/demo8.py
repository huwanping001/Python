# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/28 15:52

'''replace() 第1个参数指定被替换的子申 第2个参数指定替换子串的字符|
该方法返回替换后得到字符串替换的字符串，
替换前的字符串不发生变化，调用该方法时可以通过第3个参数指定最大替换次数字符串的合并

join() 将列表或元组中的字符|合并成一个字符串'''


s = 'hello Python'
print(s.replace('Python', 'Java'))

s1 = 'hello Python Python Python'
print(s1.replace('Python', 'Java', 2))

lst = ['hello', 'Java', 'Python']
print(' '.join(lst))

t = ('hello', 'Java', 'Python')
print(' '.join(t))

print(' '.join('Python'))


