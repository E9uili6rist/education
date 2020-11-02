n = 67834658736534870
for i in range(1, n+1):
    if n % i == 0 and i != 1:
        break
print(i)