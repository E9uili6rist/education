alp = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
       'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
word = input() + ' запретил букву'
for i in alp:
    if i in word:
        print(word.strip(), i)
    for j in word:
        if i == j:
            word = word.replace(i, '')
            word = word.replace('  ', ' ')
