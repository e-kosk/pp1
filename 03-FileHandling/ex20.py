numbers = []

with open('numbers.txt', 'r') as file:
    for line in file:
        if not int(line) % 2:
            numbers.append(int(line))

with open('evennumbers.txt', 'w') as file:
    file.write('\n'.join([str(n) for n in numbers]))
