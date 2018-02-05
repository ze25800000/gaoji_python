##### 第2章 数据结构与算法进阶训练
- [2-1 如何在列表、字典、集合中根据条件筛选数据？](#2-1-%E5%A6%82%E4%BD%95%E5%9C%A8%E5%88%97%E8%A1%A8%E5%AD%97%E5%85%B8%E9%9B%86%E5%90%88%E4%B8%AD%E6%A0%B9%E6%8D%AE%E6%9D%A1%E4%BB%B6%E7%AD%9B%E9%80%89%E6%95%B0%E6%8D%AE)
- [2-2 如何为元组中的每个元素命名，提高程序可读性？](#2-2-%E5%A6%82%E4%BD%95%E4%B8%BA%E5%85%83%E7%BB%84%E4%B8%AD%E7%9A%84%E6%AF%8F%E4%B8%AA%E5%85%83%E7%B4%A0%E5%91%BD%E5%90%8D%E6%8F%90%E9%AB%98%E7%A8%8B%E5%BA%8F%E5%8F%AF%E8%AF%BB%E6%80%A7)
- [2-3 如何统计序列中元素出现频度？](#2-3-%E5%A6%82%E4%BD%95%E7%BB%9F%E8%AE%A1%E5%BA%8F%E5%88%97%E4%B8%AD%E5%85%83%E7%B4%A0%E5%87%BA%E7%8E%B0%E9%A2%91%E5%BA%A6)
- [2-4 如何根据字典中的值的大小，对字典中的项排序？](#2-4-%E5%A6%82%E4%BD%95%E6%A0%B9%E6%8D%AE%E5%AD%97%E5%85%B8%E4%B8%AD%E7%9A%84%E5%80%BC%E7%9A%84%E5%A4%A7%E5%B0%8F%E5%AF%B9%E5%AD%97%E5%85%B8%E4%B8%AD%E7%9A%84%E9%A1%B9%E6%8E%92%E5%BA%8F)
- [2-5 如何快速找到多个字典中的公共键？](#2-5-%E5%A6%82%E4%BD%95%E5%BF%AB%E9%80%9F%E6%89%BE%E5%88%B0%E5%A4%9A%E4%B8%AA%E5%AD%97%E5%85%B8%E4%B8%AD%E7%9A%84%E5%85%AC%E5%85%B1%E9%94%AE)
- [2-6 如何让字典保持有序？](#2-6-%E5%A6%82%E4%BD%95%E8%AE%A9%E5%AD%97%E5%85%B8%E4%BF%9D%E6%8C%81%E6%9C%89%E5%BA%8F?)
- [2-7 如何实现用户的历史记录功能（最多n条）？](#2-6-%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E7%94%A8%E6%88%B7%E7%9A%84%E5%8E%86%E5%8F%B2%E8%AE%B0%E5%BD%95%E5%8A%9F%E8%83%BD%EF%BC%88%E6%9C%80%E5%A4%9An%E6%9D%A1%EF%BC%89%EF%BC%9F)

### 2-1 如何在列表、字典、集合中根据条件筛选数据
#### 列表
方式1 filter 函数
```python
from random import randint

data = [randint(-10, 10) for _ in range(10)]
# 列表
re = filter(lambda x: x >= 0, data)
```
方式2 列表解析
```python
# print(list(re))
print([x for x in re])

a = [x for x in data if x >= 0]
print(a)

```
#### 字典
```python
from random import randint

d = {x: randint(60, 100) for x in range(1, 21)}

result = {k: v for k, v in d.items() if v > 90}

print(result)

```
#### 集合
```python
from random import randint

data = [randint(-10, 10) for _ in range(10)]

s = set(data)

result = {x for x in s if x % 3 == 0}

print(result)
```

### 2-2 如何为元组中的每个元素命名，提高程序可读性？
方案一
```python
# NAME = 0
# AGE = 1
# SEX = 2
# EMAIL = 3
NAME, AGE, SEX, EMAIL = range(4)
student = ('Jim', 16, 'male', 'jim123@qq.com')
print(student[NAME])
print(student[AGE])
print(student[SEX])
print(student[EMAIL])
```
方案2
```python

from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])

s = Student('Jim', 16, 'male', 'jim123@qq.com')

print(s)
print(s.name)
print(isinstance(s, tuple)) # True

```
### 2-3 如何统计序列中元素出现频度
方法1
```python
from random import randint
data = [randint(0, 20) for _ in range(30)]
c = dict.fromkeys(data, 0)
for x in data:
    c[x] += 1
print(c)
```
方法2
```python
from collections import Counter
c2 = Counter(data)
# 出现频度最高的元素
print(c2.most_common(3))
```

案例：统计文档中出现次数最多的10个单词
```python

import re

txt = open('2-2.txt').read()

txt = re.split('\W+', txt)

c3 = Counter(txt)

print(c3)
print(c3.most_common(10))
```
###  2-4 如何根据字典中的值的大小，对字典中的项排序
方法1 利用zip将字典数据转换元组
```python
from random import randint
d = {x: randint(60, 100) for x in 'xyzabc'}
keys = d.keys()
values = d.values()
t = zip(values, keys)
print(sorted(t))
```
方法2 传递sorted函数的key参数
```python
from random import randint
d = {x: randint(60, 100) for x in 'xyzabc'}
l = d.items()
result = sorted(l, key=lambda x: x[1])
print(result)
```

###  2-5 如何快速找到多个字典中的公共键
```python
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
```

###  2-6 如何让字典保持有序?
方法1： OrderedDict
```python
from collections import OrderedDict
d = OrderedDict()
d['Jim'] = (1, 35)
d['Leo'] = (2, 37)
d['Bob'] = (3, 40)
for k in d: print(k)
```
案例
```python
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
```
# 2-7 如何实现用户的历史记录功能（最多n条）？
deque
```python
from collections import deque

deque = deque([], 5)
deque.append(1)
deque.append(2)
deque.append(3)
deque.append(4)
deque.append(5)
print(deque) # deque([1, 2, 3, 4, 5], maxlen=5)
deque.append(6)
print(deque) # deque([2, 3, 4, 5, 6], maxlen=5)
deque.append(7)
print(deque) # deque([3, 4, 5, 6, 7], maxlen=5)
```
案例
```python
from collections import deque
from random import randint

N = randint(0, 100)
history = deque([], 5)


def guess(k):
    if k == N:
        print('right')
        return True
    if k < N:
        print('%s is less-than N' % k)
    else:
        print('%s is larger-than N' % k)
    return False


while True:
    line = input("please input a number:  ")
    if line.isdigit():  # 是否是数字
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print(history)

```
