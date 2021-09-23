# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/22 16:15

items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85]

d = {item.upper(): price for item, price in zip(items,prices) }
print(d)