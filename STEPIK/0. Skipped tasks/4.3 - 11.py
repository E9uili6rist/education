a1 = 1
b1 = 2
a2 = 3
b2 = 4
if a1 > a2:
    a1, b1, a2, b2 = a2, b2, a1, b1
if b1 > a2:
    if b1 <= b2:
        print(a2, b1)
    else:
        print(a2, b2)
elif b1 == a2:
    print(b1)
elif b1 < a2:
    print('пустое множество')