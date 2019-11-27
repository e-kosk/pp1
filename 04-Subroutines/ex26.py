def podatek(dochod):
    return round(dochod * 0.17 if dochod <= 5000 else 850 + (dochod - 5000) * 0.32, 2)


d = int(input('Podaj dochód: '))
print(f'''Podatek należny: {podatek(d)} zł''')
