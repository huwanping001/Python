# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/10/13 9:21

'''getcwd()返回当前的工作目录
listdir(path)返回指定路径下的文件和目录信息
mkdir(path[,mode])创建目录
makedirs(path1/path2...[,mode])创建多级目录
rmdir(path)删除目录
removedirs(path1/path2......)删除多级目录
chdir(path)将path设置为当前工作目录'''

import os
print(os.getcwd())

lst = os.listdir('../chapter15')
print(lst)

os.mkdir('newdir')
#os.makedirs('A/B/C')

#os.rmdir('newdir')
#os.removedirs('A/B/C')

os.chdir('D:\\BIANCHENG\\pycharm\\vippython\\chapter15')
print(os.getcwd())