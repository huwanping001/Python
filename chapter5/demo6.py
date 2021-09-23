# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/18 16:00

''''输出100-999之间的水仙花数
举例：
153 = 3*3*3+5*5*5+1*1*1'''

for i in range(100, 1000):
    ge = i % 10 #个位
    shi = i // 10 % 10  #十位
    bai = i // 100 #百位
    #print(ge, shi, bai)
    #判断
    if ge**3 + shi**3 + bai**3 == i:
        print(i, '是水仙花数')