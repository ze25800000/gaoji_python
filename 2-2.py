# 如何为元组中的每个元素命名，提高程序可读性？

# 方案一

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

# 方案2

from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])

s = Student('Jim', 16, 'male', 'jim123@qq.com')

print(s)
print(s.name)
print(isinstance(s, tuple)) # True
