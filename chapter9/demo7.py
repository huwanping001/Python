# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/28 11:18

'''isidentifier() 判断指定的字符串是不是合法的标识符
isspace()判断指的字符串是否全部由空白字符组成（回车、换行，水平制表符）
isalpha()判断指定的字符串是否全部由字母组成
isdecimal()判断指定字符串是否全部由十进制的数字组成
isnumeric()判断指定的字符串是否全部由数字组成
isalnum（）断指定字符出是否全部由字母和数字组成'''


s = 'hello,python'
print('1.', s.isidentifier()) #False
print('2.', 'hello'.isidentifier()) #True
print('3.', '张三_'.isidentifier()) #True
print('4.', '张三_123'.isidentifier()) #True

print('5.', '\t'.isspace()) #True

print('6.', 'abc'.isalpha()) #True
print('7.', '张三'.isalpha()) #True
print('8.', '张三1'.isalpha()) #False

print('9.', '123'.isdecimal()) #True
print('10.', '123四'.isdecimal()) #False
print('11.', ''.isdecimal()) #False

print('12.', '1230'.isnumeric())#True
print('13.', '123四'.isnumeric())#True
print('14.', ''.isnumeric()) #True

print('15.', 'abcl'.isalnum())#True
print('16.', '张三123'.isalnum())#True
print('17.', 'abc!'.isalnum())#False



