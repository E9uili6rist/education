n = int(input())
s = []
for i in range(1, n+1):
    x = input()
    if x not in s:
        s.append(x)
    else:
        continue
print(*s, sep='\n')