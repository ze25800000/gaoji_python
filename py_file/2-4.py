# 2-4 如何根据字典中的值的大小，对字典中的项排序
# 方法1 利用zip将字典数据转换元组
from random import randint

d = {x: randint(60, 100) for x in 'xyzabc'}
keys = d.keys()
values = d.values()
t = zip(values, keys)
print(sorted(t))

# 方法2 传递sorted函数的key参数
l = d.items()
result = sorted(l, key=lambda x: x[1])
print(result)
