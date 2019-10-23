k = int(input("Podaj kwotę: "))
m5 = k // 5
m2 = (k - m5 * 5) // 2
m1 = k - m5 * 5 - m2 * 2
print(f"5 zł - {m5} szt")
print(f"2 zł - {m2} szt")
print(f"1 zł - {m1} szt")
