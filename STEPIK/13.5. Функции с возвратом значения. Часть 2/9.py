def is_correct_bracket(text):
    count = 0
    if text[0] != '(' and text[-1] != ')':
        return 'False'

    for i in text:
        if i == '(':
            count += 1
        else:
            count -= 1
            if count == -1:
                return False

    if count == 0:
        return True
    else:
        return False


txt = input()

print(is_correct_bracket(txt))