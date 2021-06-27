amount = int(input())
spisok = []
spisok_sum = []
for i in range(amount):
    spisok.append(int(input()))
for i in range(amount - 1):
    sum = spisok[i] + spisok[i + 1]
    spisok_sum.append(sum)
print(spisok_sum)