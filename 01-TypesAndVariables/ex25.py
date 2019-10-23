nr = input("Podaj nr rachunku: ")
print(' '.join([nr[i:i+4] if i > 0 else nr[:2] for i in range(-2, 26, 4)]))
