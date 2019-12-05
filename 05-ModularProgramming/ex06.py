import csv


with open('employees.csv', newline='') as f:
    reader = csv.DictReader(f)
    print(f'''{'#':<5}{reader.fieldnames[1].upper():20}{reader.fieldnames[0].upper():20}{reader.fieldnames[2].upper():10}{reader.fieldnames[3].upper():10}''')
    print('=' * 70)
    for index, row in enumerate(reader):
        print(f'''{index + 1:<5}{row['name'].upper():20}{row['surname']:20}{row['age']:10}{row['email']:10}''')
