# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/22 15:14

'''获取字典的元素'''
score = {'xiaohu': 98, 'xiaolan': 100, 'xiaobai': 99}

'''第一种方式，使用[]'''
print(score['xiaohu'])
#print(score['xiaoqiang']) #KeyError: 'xiaoqiang'

'''第二种方式，使用get()方法'''
print(score.get('xiaohu'))
print(score.get('xiaoqiang')) #None
print(score.get('xiaoai', 99)) #99是查找字典‘xiaoai’不存在时指定的默认值
