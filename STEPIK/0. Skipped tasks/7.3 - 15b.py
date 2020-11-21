n = 5
total_1 = 0
total_2 = 1
for i in range(n):
    print(total_2, end=' ')
    # развернутый вариант присвоения
    x = total_2
    total_2 = total_1 + total_2
    total_1 = x

