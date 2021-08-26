def caesar(text):
    text = text.split()
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwzyx'
    crypter_word = []
    crypter_letter = ''

    for word in text:
        key = 0
        for i in word:
            if i in alph:
                key += 1
            else:
                continue
        for letter in word:
            if 65 <= ord(letter) <= 90:
                crypter_letter = chr((((ord(letter) - 65) + key) % 26) + 65)
                crypter_word.append(crypter_letter)
            elif 97 <= ord(letter) <= 122:
                crypter_letter = chr((((ord(letter) - 97) + key) % 26) + 97)
                crypter_word.append(crypter_letter)
            else:
                crypter_word.append(letter)
        crypter_word.append(' ')

    return ''.join(crypter_word)


text = input()
print(caesar(text))