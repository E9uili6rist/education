n = 100
total_1 = 0
total_2 = 1
for i in range(n):
    print(total_2, end=' ')
    total_2, total_1 = total_1 + total_2, total_2     # лаконичный вариант присвоения




