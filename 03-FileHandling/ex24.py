import csv

tab = [['Marek', 'Zelnik', 'zelnik@sed.pl'],
       ['Ewa', 'Maj', 'maje@wp.pl'],
       ['Piotr', 'Wyga', 'wygap@gop.pl']]

header = ['Imie', 'Nazwisko', 'Email']

with open('ex24file.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(header)
    for line in tab:
        writer.writerow(line)
