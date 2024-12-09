import random
from random import randint

res = []
for i in range(100000):
    res.append(randint(1, 100000))

print(*res)