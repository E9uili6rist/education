count = 0
s = input().split()
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            count += 1
print(count)