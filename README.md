- [2-1 如何在列表、字典、集合中根据条件筛选数据](#2-1)
- [2-2 如何为元组中的每个元素命名，提高程序可读性？](#2-2)
- [2-3 如何统计序列中元素出现频度](#2-3)
- [2-4 如何根据字典中的值的大小，对字典中的项排序](#2-4)

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

###  2-5 如何快速找到多个字典中的工共建
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