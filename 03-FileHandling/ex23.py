import re

with open('land.txt', 'r') as file:
    print(sum([int(n) for n in re.findall(r'\d', file.read())]))
