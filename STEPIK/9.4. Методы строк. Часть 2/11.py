s = input()
count = 0
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        count += 1
print(count)