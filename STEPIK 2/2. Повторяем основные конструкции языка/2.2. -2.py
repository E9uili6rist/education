stroka = input()
spisok = stroka.split()
count = 0
count2 = 0
for i in range(len(spisok)):
    count2 += 1
    if count2 == len(spisok):
        break
    if int(spisok[i + 1]) > int(spisok[i]):
        count += 1

print(count)