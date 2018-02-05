# 如何在列表，字典，集合中更具条件筛选数据

from random import randint

data = [randint(-10, 10) for _ in range(10)]

s = set(data)

result = {x for x in s if x % 3 == 0}

print(result)
