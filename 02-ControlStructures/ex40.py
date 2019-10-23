from random import randint

r = [randint(1,6) for _ in range(100)]
print(f'Szóstka: {r.count(6)}')
print(f'Piątka: {r.count(5)}')
print(f'Czwórka: {r.count(4)}')
print(f'Trójka: {r.count(3)}')
print(f'Dwójka: {r.count(2)}')
print(f'Jedynka: {r.count(1)}')
