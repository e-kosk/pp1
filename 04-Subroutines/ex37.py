def foo(tab):
    return [val for val in tab if tab.count(val) == 1]


t = [1, 1, 1, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 7, 8, 9, 9]
print(foo(t))
