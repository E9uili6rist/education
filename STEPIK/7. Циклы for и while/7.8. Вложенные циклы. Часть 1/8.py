n = 5
for i in range(n//2):
    for j in range(i+1):
        print('*', end='')
    print()
m = n//2
for i in range(m):
    print ('*', end='')
for i in range(n//2):
    for j in range(-i):
        print('*', end='')
    print()