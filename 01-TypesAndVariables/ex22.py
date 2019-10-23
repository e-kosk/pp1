a = int(input("Podaj pierwszy bok: "))
b = int(input("Podaj drugi bok: "))
c = int(input("Podaj trzeci bok: "))
f = (((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) ** (1 / 2)) / 4
print(f"Pole trójkata wynosi: {f}")
