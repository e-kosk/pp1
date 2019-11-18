import csv

with open('students.txt', 'r') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        if int(row['age']) < 30:
            print(f"""{row['first_name']:10}{row['last_name']:10}{row['email']:20}""")
