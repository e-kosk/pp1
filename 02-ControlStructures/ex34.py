p = input('Podaj PESEL: ')
print(f"Płeć: {'mężczyzna' if int(p[-2]) % 2 else 'kobieta'}")
print(f'Wiek: {118 - int(p[:2])}')
