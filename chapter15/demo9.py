# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/10/11 11:22

file = open('a.txt', 'r')
file.seek(2)
print(file.read())
print(file.tell())
file.close()
