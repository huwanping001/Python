#输出函数print

#输出数字
print(520)
print(98.50)

#输出字符串
print("xiaohu")

#输出表达式
print(3+1)

#上面三种均为输出目的地可以为控制台和文件中


#输出到文件中 注意  1所指定盘符存在  2.使用file = fp
fp = open('D:/text.txt','a+')  # a+ 如果文件不存在就创建，存在就在文件内容后面进行追加
print('woaixiaohu',file=fp)
fp.close()

#不进行换行输出

print('hello','xiao','hu')


