import csv


with open('employees.csv', newline='') as f:
    reader = csv.DictReader(f)
    print(f'''{reader.header()}''')
    for index, row in enumerate(reader):
        print(f'''{index + 1:<5}{row['name']:20}{row['surname']:20}{row['age']:10}{row['email']:10}''')
