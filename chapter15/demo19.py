# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/10/13 9:53

import os
path = os.getcwd()
lst_files = os.walk(path)
for dirpath, dirname, filename in lst_files:
    '''print(dirpath)
    print(dirname)
    print(filename)
    print('------------------------------')'''
    for dir in dirname:
        print(os.path.join(dirpath, dir))

    for file in filename:
        print(os.path.join(dirpath, file))

    print('-------------------------------')