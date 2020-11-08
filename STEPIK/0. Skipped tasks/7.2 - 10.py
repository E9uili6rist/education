m = 1
n = 20
for i in range(m, n+1):
    if i % 17 == 0:
        print(i)
    elif i % 15 == 0:
        print(i)
    elif str(i)[-1] == "9":
        print(i)
