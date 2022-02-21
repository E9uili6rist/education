stroka = input()
spisok = stroka.split()
test = []
count = 0

for i in spisok:
    if i in test:
        continue
    if i not in test:
        test.append(i)
        count += 1

print(count)