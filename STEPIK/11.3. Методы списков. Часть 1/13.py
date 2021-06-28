amount = int(input())
spisok = []
for i in range(amount):
    spisok.append(input())
nomer = int(input())
result = ''
for i in spisok:
    if nomer > len(i):
        continue
    else:
        result += i[nomer - 1]
print(result)