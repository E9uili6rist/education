s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])
a = s.index(max(s))
b = s.index(min(s))
x = max(s)
y = min(s)
s[a] = y
s[b] = x
print(*s)