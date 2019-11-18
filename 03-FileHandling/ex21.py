numbers = []

with open('numbersinrows.txt', 'r') as file:
    for line in file:
        for number in line.split(','):
            numbers.append(int(number))

print(f'liczb: {len(numbers)}')
print(f'suma: {sum(numbers)}')
