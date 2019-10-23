a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + d ** (1/2)) / 2 * a
    x2 = (-b - d ** (1/2)) / 2 * a
    print(f'x1: {x1}\nx2: {x2}')
elif d == 0:
    x0 = -b / (2 * a)
    print(f'x0: {x0}')
else:
    print('brak rozwiązań')
