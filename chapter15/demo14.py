# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/10/13 9:01

with open('logo.png', 'rb') as src_file:
    with open('copy2logo.png', 'wb') as target_file:
        target_file.write(src_file.read())