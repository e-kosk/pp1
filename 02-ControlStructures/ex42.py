x = int(input('Podaj liczbę: '))
y = int(input('Podaj liczbę: '))
try:
    print(f'Wynik: {x/y}')
except ZeroDivisionError:
    print('Dzielenie przez 0!')
