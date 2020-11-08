n = 10
total = 0
for i in range(n):
    for j in range(i + 1):
        total += 1
        print(total, end="")
    for j in range(i + 1):
        total -= 1
        if total == 0:
            break
        print(total, end="")
    print()
