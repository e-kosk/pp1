def foo(n):
    n = str(n)
    if len(n) > 1:
        return foo(n[1:]) + int(n[0])
    else:
        return int(n)


print(foo(754016))

