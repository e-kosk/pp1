def wystepuje(liczba, tablica):
    print(f'''Liczba: {liczba}''')
    print(f'''Tablica: {' '.join([str(i) for i in tablica])}''')
    print(f'''Podana liczba {'nie występuje' if not liczba in tablica else 'występuje'} w tablicy.''')


tab = [15, 38, 7, 23, 14]

wystepuje(23, tab)
