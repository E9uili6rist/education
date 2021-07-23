import random

digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
n_punctuation = 'il1LoO0'
chars = ''
counter = 0

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password


while True:
    print('Количество паролей?')
    count = int(input())
    print('Длина пароля?')
    length = int(input())
    print('Включать цифры? (да/нет)')
    digit = input()
    if digit == 'да':
        chars += digits
    else:
        counter += 1
    print('Включать прописные буквы? (да/нет)')
    upper = input()
    if upper == 'да':
        chars += uppercase_letters
    else:
        counter += 1
    print('Включать строчные буквы? (да/нет)')
    lower = input()
    if lower == 'да':
        chars += lowercase_letters
    else:
        counter += 1
    print('Включать символы? (да/нет)')
    symbols = input()
    if symbols == 'да':
        chars += punctuation
    else:
        counter += 1
    print('Исключать неоднозначные символы "il1Lo0O" (да/нет)')
    n_symbols = input()
    if n_symbols == 'нет':
        chars += n_punctuation
    else:
        counter += 1
    print(counter)
    if counter < 5:
        break
    if counter == 5:
        print('Для генерации пароля необходимо указать хотя бы один из предложенных парметров помимо количества и длины.')
        continue

for i in range(count):
    print(generate_password(length, chars))




