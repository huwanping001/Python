# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/28 10:58

'''
center()居中对齐，第1个参数指定宽度，第2个参数指定填充符，第2个参数是可选的，
默认是空格，如果录置克实小于实际宽度则则返回原字符申左对齐，

ljust()第1个参数指元觅度，第2个参数指定填充符，第2个参数是可选的，
默认是空格如果设置宽度小于实际宽度则则返回厅字符串

rjust()右对齐，第1个参数指定宽度，第2个参数指定填充符，
第2个参数是可选的，默认是空格如果设置宽度小于实际宽度则则返回原字符串

zfill( )右对齐，左边用0填充，该方法只接收一个参数，用于指元了符串的宽度，
如果指元的宽度小于等于字符串的长度，返回字符串本身
'''

s = 'hello Python'
'''居中对齐'''
print(s.center(20, "*"))

'''左对齐'''
print(s.ljust(20, "*"))
print(s.ljust(10))
print(s.ljust(20))

'''右对齐'''
print(s.rjust(20, "*"))
print(s.rjust(10))
print(s.rjust(20))

'''右对齐，使用0进行填充'''
print(s.zfill(20))
print(s.zfill(10))
print('-8910'.zfill(8))