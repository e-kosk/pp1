from random import randint


def rand():
    return randint(1, 50)


numbers = [rand() for _ in range(1000)]
p = []
n = []
for number in numbers:
    if not number % 2:
        p.append(number)
    else:
        n.append(number)

print('Dla 1000 liczb losowych z przedziału <1, 50>:')
print(f'''Liczby parzyste: {len(p) / 10}%''')
print(f'''Liczby nieparzyste: {len(n) / 10}%''')