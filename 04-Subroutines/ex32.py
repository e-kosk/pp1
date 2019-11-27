def tanspozycja(macierz):
    tm = [[macierz[j][i] for j in range(len(macierz))] for i in range(len(macierz[0]))]
    return tm


def wys(m):
    for y in m:
        for x in y:
            print(x, end=' ')
        print()


m1 = [[1, 2, 0], [0, 0, 3], [5, 1, 1]]
tm1 = tanspozycja(m1)

wys(m1)
print()
wys(tm1)
