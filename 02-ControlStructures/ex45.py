limit = int(input("Podaj liczbę: "))
tab = []
n = 2
while len(tab) < limit:
    for x in range(2, n):
        if (n % x) == 0:
            break
    else:
       tab.append(n)
    n += 1
print('Liczby pierwsze: ')
print(tab)
