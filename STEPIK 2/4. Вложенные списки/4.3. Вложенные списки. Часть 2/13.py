def chunked(lst, num):
    for i in range(0, len(stroka), num):
        lst.append(stroka[i:i + num])
    return lst


stroka = input().split()
num = int(input())
lst = []
print(chunked(lst, num))