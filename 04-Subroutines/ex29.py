def med(tab):
    tab = sorted(tab)
    l = len(tab)
    if not l % 2:
        return (tab[l // 2] + tab[(l // 2) + 1]) / 2
    else:
        return tab[l // 2]


def dom(tab):
    return max(tab, key=tab.count)


tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]

print(med(tab))
print(dom(tab))
