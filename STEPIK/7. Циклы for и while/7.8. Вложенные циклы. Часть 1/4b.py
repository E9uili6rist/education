n = 5
total = 0
for i in range(n):
    for j in range(i+1):
        total += 1
        print(total, end='')
    print()
