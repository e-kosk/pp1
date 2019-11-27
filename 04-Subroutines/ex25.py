def jestImie(imie, imiona):
    print(f'''Imiona: {' '.join(imiona)}''')
    print(f'''Imie: {imie}''')
    print(f'''Rezultat: imie {'zawarte jest' if imie in imiona else 'nie jest zawarte'} w wykazie imion.''')


names = ['Janek', 'Ania', 'Wojtek', 'Zosia']
name = 'Janek'

jestImie(name, names)
