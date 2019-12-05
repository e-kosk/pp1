import csv
import statistics as s


with open('employees.csv', 'r') as f:
    reader = csv.DictReader(f)
    ages = [int(worker['age']) for worker in reader]
    mean = s.mean(ages)
    median = s.median(ages)
    stdev = s.stdev(ages)

print(f'Średnia: {mean}')
print(f'Mediana: {median}')
print(f'Odchylenie standardowe: {stdev}')
