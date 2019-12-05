def display_raport(data:dict):
    months = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec']
    print('RAPORT Z WYDATKÓW')
    print(f'{"MIESIĄC":<10}{"WYDATKI":>10}')
    print('-' * 20)
    for month, expenses in zip(months, data):
        print(f'{month:<10}{expenses:10}')


def display_statistics(data):
    statistics_names = ['średnia', 'mediana', 'minimum', 'maximum']
    print('STATYSTYKA WYDATKÓW')
    print('-' * 20)
    for n, d in zip(statistics_names, data):
        print(f'{n:<10}{d:10}')


def display_chart(data):
    months = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec']
    print('GRAFICZNA REPREZENTACJA WYDATKÓW')
    print('-' * 20)
    for month, expenses in zip(months, data):
        print(f'{month:<10}{"#" * round(expenses / 50)}')


def sep(n):
    print('\n')
    print('=' * n)
    print('\n')
