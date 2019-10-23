x = 1
while True:
    if x % 2 == 1 \
            and x % 3 == 1 \
            and x % 4 == 1 \
            and x % 5 == 1 \
            and x % 6 == 1 \
            and not x % 7:
        print(x)
        break
    x += 1
