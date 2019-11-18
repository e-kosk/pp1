with open('numbers.txt', 'r') as file:
    print(sum([int(i) for i in file]))
