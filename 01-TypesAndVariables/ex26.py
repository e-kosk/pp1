wzrost = float(input("podaj wzrost w m: "))
waga = int(input("podaj wagę w kg: "))
BMI = waga / (wzrost ** 2)
print(f'Wskaźnik BMI: {BMI}', '(waga prawidlowa)' if 25 > BMI > 18.5 else '(waga nieprawidłowa)')
