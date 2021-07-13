def convert_to_python_case(text):
    s = []
    for i in text:
        if i in '0123456789':
            s.append(i)
        if i == i.lower() and i.isalpha():
            s.append(i)
        if i == i.upper() and i.isalpha():
            s.append('_')
            s.append(i.lower())

    return ''.join(s[1:])


txt = input()

print(convert_to_python_case(txt))