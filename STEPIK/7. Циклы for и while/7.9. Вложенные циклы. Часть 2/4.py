n = 5
counter = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        if i % j == 0:
            counter += 1
    print(i, counter * '+', sep='')
    counter = 0
print()