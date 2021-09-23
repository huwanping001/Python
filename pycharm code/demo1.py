#6.转义字符  同C语言一样 \加需要转义的字符

print('xiao\nhu') #换行
print('xiao\thu') #制表
print('xiaohuh\tu')#指表位4个空格，占满4则重开制表位，否则不重开
print('xiao\rhu') #覆盖
print('xiao\bhu')#退一格 把o给退没了

print('http:\\\\www.baidu.com')
print('老师说：\'大家好\'')

#原字符 ，不希望字符串中的转义字符起作用，就是用原字符，就是在字符串之前加上R或r
print(r'xiao\nhu')
#注意事项，最后一个字符不能是\
#print(r'xiaohu\')
