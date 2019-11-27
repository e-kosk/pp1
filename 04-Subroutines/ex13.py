def suma(tablica):
    print(f'''Tablica: {' '.join(str(i) for i in tablica)}''')
    print(f'''Suma wartości: {sum(i for i in tab if isinstance(i, int))}''')


tab = [4, 3, 7, 1, 3]

suma(tab)
