counter = True
numbers = input().split('.')
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    if not 0 <= numbers[i] <= 255:
        counter = False
        break
if counter == False:
    print('НЕТ')
else:
    print('ДА')