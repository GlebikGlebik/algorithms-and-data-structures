import random
from random import randint

res = []
for i in range(100000):
    res.append(randint(1, 1000000))

print(*res)