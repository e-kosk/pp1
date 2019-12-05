import re


def czytajWspolczynniki():
    equation = input('Równanie kwadratowe w postaci: ').replace(' ', '')

    a_regex = re.findall(r'(?P<a>-?\d+)x2', equation)
    a = a_regex[0] if a_regex else 1

    b_regex = re.findall(r'(?P<b>-?\d+)x[^\d]', equation)
    b = b_regex[0] if b_regex else 1

    c_regex = re.findall(r'[^x](?P<c>-?\d+)[^x\d]', equation)
    c = c_regex[0] if c_regex else 0

    return [a, b, c]


def obliczDelte(list_abc):
    a = int(list_abc[0])
    b = int(list_abc[1])
    c = int(list_abc[2])
    delta = b**2 - 4 * a * c
    return delta


def obliczPierwiastki(list_abc):
    a = int(list_abc[0])
    b = int(list_abc[1])
    c = int(list_abc[2])
    delta = obliczDelte(list_abc)
    if delta > 0:
        sqrt_delta = delta ** (1/2)
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        return [x1, x2]
    elif delta == 0:
        x0 = -b / (2*a)
        return [x0]
    else:
        return []


def wyswietlPierwistki(list_x1_x2_x0):
    if len(list_x1_x2_x0) == 2:
        print(f'Pierwiastki równania: x1 = {list_x1_x2_x0[0]}, x2 = {list_x1_x2_x0[1]}')
    elif len(list_x1_x2_x0) == 1:
        print(f'Pierwiastek równania: x = {list_x1_x2_x0[0]}')
    else:
        print('Brak rozwiązań równania')
