def rysujWykres(jezyki, wartosci):
    for j, w in zip(jezyki, wartosci):
        print(f'''{j:>10}: {'#' * (w // 3)}''')


jezyki = ['Java', 'Python', 'JavaScript', 'C++', 'C#', 'Ruby', 'Perl', 'PHP', 'C', 'Android']
wartosci = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]

rysujWykres(jezyki, wartosci)
