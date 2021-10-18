# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/10/9 20:12

import schedule
import time

def job():
    print('哈哈')


schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
