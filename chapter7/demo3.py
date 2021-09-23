# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/22 15:20

''':key的判断'''
score = {'xiaohu': 98, 'xiaolan': 100, 'xiaobai': 99}
print('xiaohu' in score)
print('xiaohu' not in score)

del score['xiaohu'] #删除指定的key-value对
#score.clear() #清空字典元素
print(score)

score['xiaoliu'] = 88 #新增元素
print(score)

score['xiaoliu'] = 97 #修改元素
print(score)
