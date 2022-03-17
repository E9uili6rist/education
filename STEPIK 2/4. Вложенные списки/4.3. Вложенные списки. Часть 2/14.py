stroka = input().split()

new_list = [[]]

for len_substr in range(len(stroka)):
    for i in range(len(stroka) - len_substr):
        new_list.append(stroka[i: i + len_substr + 1])

print(new_list)