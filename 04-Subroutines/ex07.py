def keypad():
    for y in range(1, 9, 3):
        for x in range(3):
            print(x+y, end='')
        print()


keypad()
