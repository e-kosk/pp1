from random import randint

u = int(input("Podaj swoją liczbę: "))
k = randint(1, 6)
print(f'Komputer wyrzucił: {k}')
print(f'Zgadłeś: {u == k}')
