n = int(input())
s = []
for i in range(n):
    s.append(input())
k = int(input())
kstr = []
for i in range(k):
    kstr.append(input())
for big_word in s:
    sovpadenie = 0
    for small_word in kstr:
        if small_word.lower() in big_word.lower():
            sovpadenie += 1
    if sovpadenie == k:
        print(big_word)