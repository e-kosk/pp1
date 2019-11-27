from random import randint


def rzucKostka():
    return randint(1, 6)


res = [rzucKostka() for _ in range(3)]

print(f'''Wyrzucone oczka: {' '.join([str(i) for i in res])}''')
print(f'''Suma oczek: {sum(res)}''')
