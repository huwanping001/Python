# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/28 11:10

'''
split() 从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
以通过参数sep指定劈分字符串是的劈分符
通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独做为一部分

rsplit()从字符串的右边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
 以通过参数sep指定劈分字符串是的劈分符
通过参数maxsplit指儿劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独做为一部分'''

s = 'hello world Python'
lst = s.split()
print(lst)

s1 = 'hello|world|Python'
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))

'''rsplit()从右侧开始劈分'''
print('------------------------')
print(s1.rsplit())
print(s1.rsplit("|"))
print(s1.rsplit(sep='|', maxsplit=1))