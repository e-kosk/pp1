import random

s = 0

for _ in range(3):
    n = random.randint(1, 6)
    print(n)
    s += n

print(s)
