def countdown(i):
    print(i, end=' ')
    if i <= 1:
        return
    else:
        countdown(i-1)


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


countdown(3)
print()
print(fact(3))    