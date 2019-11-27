def miesiac(n):
    months = ['styczen', 'luty', 'marzec', 'kwiecien', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrzesien',
              'pazdziernik', 'listopad', 'grudzien']
    return months[n - 1]


print(miesiac(7))
print(miesiac(9))
