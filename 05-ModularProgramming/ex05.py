import statistics as s


tab = [21600, 4350, 3920, 5590, 3250, 4010]

print(f'Srednia: {s.mean(tab)}')
print(f'Mediana: {s.median(tab)}')
print(f'Odchylenie standardowe: {s.stdev(tab)}')
