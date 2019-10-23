nr = int(input("Podaj nr dnia tygodnia: "))
dni_tygodnia = ['PN', 'WT', 'ŚR', 'CZ', 'PT', 'SB', 'ND']
print(f'| {" | ".join(dni_tygodnia)} |')
for x in range(1 - nr, 31):
    if x > 0:
        if not x % 7:
            print()
        print(f'| {x:2} ', end='')
    else:
        print(f'|    ', end='')