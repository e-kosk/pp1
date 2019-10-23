x, y = 0, 1
for _ in range(50):
    print(x, end=' ')
    x, y = y, x+y
