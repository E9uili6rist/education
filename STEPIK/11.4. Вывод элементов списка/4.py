n = int(input())
s = []
for i in range(1, n+1):
    s.append(int(input()))
del s[s.index(min(s))]
del s[s.index(max(s))]
print(*s, sep ='\n')