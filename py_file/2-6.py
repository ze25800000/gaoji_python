# 如何让字典保持有序?
# 方法1
from collections import OrderedDict
from time import time
from random import randint

d = OrderedDict()
players = list('ABCDEFGH')
start = time()
for i in range(7):
    input()
    index = randint(0, 7 - i)
    p = players.pop(index)
    end = time()
    print(i + 1, p, end - start)
    d[p] = (i + 1, end - start)

print('-' * 20)

for k in d:
    print(k, d[k])
