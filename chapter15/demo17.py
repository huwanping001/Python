# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/10/13 9:34


'''abspath(path) 用于获取文件或目录的绝对路径
exists(path)用于判断文件或目录是否存在，如果存在返回True,否则返回False
join(path, name)将目录与目录或者文件名拼接起来
splitext()分离文件名和扩展名
basename(path)从一个目录中提取文件名
dirname(path)从一个路径中提取文件路径，不包括文件名
isdir(path) 用于判断是否为路径'''


import os.path
print(os.path.abspath('demo13.py'))
print(os.path.exists('demo13.py'), os.path.exists('demo18.py'))
print(os.path.join('D:\\Python', 'demo13.py'))
print(os.path.split('D:\\BIANCHENG\\pycharm\\vippython\\chapter15'))
print(os.path.splitext('demo13.py'))
print(os.path.basename('D:\\BIANCHENG\\pycharm\\vippython\\chapter15\\demo13.py'))
print(os.path.dirname('D:\\BIANCHENG\\pycharm\\vippython\\chapter15\\demo13.py'))
print(os.path.isdir('D:\\BIANCHENG\\pycharm\\vippython\\chapter15\\demo13.py'))