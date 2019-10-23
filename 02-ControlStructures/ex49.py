nr = int(input("Podaj nr dnia tygodnia: "))
dni_tygodnia = ['PN', 'WT', 'ŚR', 'CZ', 'PT', 'SB', 'ND']
print(f'| {" | ".join(dni_tygodnia)} |')
for x in range(1 - nr, 31):
    if x > 0:
        print(f'| {x:2} ', end='')
        if not (x + nr) % 7:
            print('|')
    else:
        print(f'|    ', end='')
