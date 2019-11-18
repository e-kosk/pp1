with open('NoEducation.txt', 'r') as file:
    for line in enumerate(file):
        print(line[0] + 1, line[1], end='')
