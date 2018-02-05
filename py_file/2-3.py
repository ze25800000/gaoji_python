# 如何统计序列中元素出现频度

from random import randint

# 方法1
data = [randint(0, 20) for _ in range(30)]

c = dict.fromkeys(data, 0)

for x in data:
    c[x] += 1

print(c)

# 方法2
from collections import Counter

c2 = Counter(data)
# 出现频度最高的元素
print(c2.most_common(3))

# 方法3

import re

txt = open('2-2.txt').read()

txt = re.split('\W+', txt)

c3 = Counter(txt)

print(c3)
print(c3.most_common(10))
