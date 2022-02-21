n = int(input())
k = int(input())
x = 0
for i in range(1, n+1):
    x = (x + k) % i
print(x + 1)
