# 学校：四川轻化工大学
# 学院：自信学院
# 学生：胡万平
# 开发时间：2021/9/29 10:22

def fun(a, b, c): #a,b,c是形式参数
    print('a =', a)
    print('b =', b)
    print('c =', c)

#函数的调用
fun(10, 20, 30) #函数调用时的参数传递，称为位置实参
lst = [11, 22, 33]
fun(*lst)  #在函数调用时，将列表中的每个元素都转为位置实参传入

fun(a = 100, b = 200, c = 300) #函数的调用，所以是关键字实参
dic = {'a': 111, 'b': 222, 'c': 333}
fun(**dic)  #在函数调用时，将字典中的键值对都转为关键字实参



