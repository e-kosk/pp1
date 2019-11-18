tab = [32, 16, 5, 8, 24, 7]

with open('ex13file.txt', 'w') as file:
    file.write('\n'.join([str(n) for n in tab]))
