import re


def up(s):
    return ''.join(re.findall(r'[A-Z]', s))


print(up('Ala Ma Kota'))
