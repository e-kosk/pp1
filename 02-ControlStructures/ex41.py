tab = []
while True:
    x = int(input("Podaj liczbę: "))
    if x == 0:
        print(f'REZULTAT: Liczb={len(tab)}, Suma={sum(tab)}, Średnia={sum(tab) / len(tab)}')
        break
    tab.append(x)
