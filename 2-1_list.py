# 如何在列表，字典，集合中根据条件筛选数据

from random import randint

data = [randint(-10, 10) for _ in range(10)]
# 列表
# 方式1 filter 函数
re = filter(lambda x: x >= 0, data)

# print(list(re))
print([x for x in re])

# 方式2 列表解析
a = [x for x in data if x >= 0]
print(a)
