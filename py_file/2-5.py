# 2-5 如何快速找到多个字典中的工共建
from functools import reduce
from random import randint, sample

s = sample('abcdefg', randint(3, 6))

s1 = {x: randint(1, 4) for x in s}
s2 = {x: randint(1, 4) for x in s}
s3 = {x: randint(1, 4) for x in s}
# 方法1
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)
print(res)
# 方法2 利用集合的交集操作
print(s1.keys() & s2.keys() & s3.keys())

# map得到所有字典的keys的集合
l = map(dict.keys, [s1, s2, s3])

# reduce得到所有字典的keys的集合的交集
reduce(lambda a, b: a & b, l)
