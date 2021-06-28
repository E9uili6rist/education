n = int(input())
s = []
for i in range(1, n+1):
    s.append(int(input()))
print(*s, sep ='\n')
print()
s2 = []
for num in s:
    x = num**2 + 2*num + 1
    s2.append(x)
print(*s2, sep ='\n')