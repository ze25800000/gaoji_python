from random import randint

d = {x: randint(60, 100) for x in range(1, 21)}

result = {k: v for k, v in d.items() if v > 90}

print(result)
