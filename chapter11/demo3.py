# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/29 18:51

'''● 第一层for循环遍历列表可以得到每一部电影，而每一部电影又是一个字典，只需要根据key在字典中取值即可。
根据演员的键actors取出学员的列表，使用判断name在列表中是否存在，最后根据电影名称的键title取出电影的名称，进行输出'''
lst=[{'rating':[9.7,50],'id':'1292052','type':['犯罪','剧情'],'title':'肖申克的救赎','actors':['蒂姆.罗宾斯','摩根.弗里曼']},
     {'rating':[9.6,50],'id':'1291546','type':['剧情','爱情','同性'],'title':'霸王别姬','actors':['张国荣','张丰毅','巩俐','葛优']},
      {'rating':[9.6,50],'id':'1296141','type':['剧情','犯罪','悬疑'],'title':'控方证人','actors':['泰隆.鲍华','玛琳.黛德丽']}]

name = input('请输入你要查询的演员：')
for item in lst: #遍历列表，item又是一个字典
    act_lst = item['actors']
    for actor in act_lst:
        if name in actor:
            print(name, '出演了', item['title'])

