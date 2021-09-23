# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/17 20:36

#布尔运算符

# and
print('----------------------and 并且-----------------')
a, b = 1, 2
print(a == 1 and b == 2) #True   True and True --> True
print(a == 1 and b < 2) #False   True and False --> False
print(a != 1 and b == 2) #False False and True --> False
print(a != 1 and b != 2) #False False and False --> False

# or
print('----------------------or 或者-----------------')
print(a == 1 or b == 2) #True  True or True -->True
print(a == 1 or b < 2)  #True  True or False -->True
print(a != 1 or b == 2) #True  False or True -->True
print(a != 1 or b != 2) #False False or False -->False

# not
print('---------------------not 对bool类型操作数取反-----------')
f1 = True
f2 = False
print(not f1) # False
print(not f2) # True

# in
print('---------------------in 与 not in------------------')
s = 'xiaohu'
print('x' in s) #True
print('w' in s) #False
print('x' not in s) #False
print('w' not in s) #True


