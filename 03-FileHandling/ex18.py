tab = []

with open('numbers.txt', 'r') as file:
    for line in file:
        tab.append(line.strip())

print(' '.join(sorted(tab)))
