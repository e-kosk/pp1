l = int(input('Limit prędkości: '))
p = int(input('Podaj prędkość: '))
if (p - l) <= 10:
    print(f'Mandat: {(p - l) * 5} zł')
else:
    print(f'Mandat: {50 + ((p - l - 10) * 15)} zł')
