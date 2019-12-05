import re


def get_data(file):
    with open(file, 'r') as f:
        expenses = re.findall(r'(?P<n>\d[\d.]*)\szł', f.read())
    return [float(n) for n in expenses]
