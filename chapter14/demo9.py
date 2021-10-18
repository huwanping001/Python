# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/10/7 21:15

#导入带有包的模块时注意事项

import package1
import calc
#使用import方式进行导入时，只能跟模块名或者包名

from package1 import module_A
from package1.module_A import a
#使用from...import可以导入包，模块，函数，变量