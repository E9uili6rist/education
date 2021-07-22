import random


def is_valid(arg):
    if arg.isdigit():
        if 1 <= int(arg) <= int(n):
            return True
        else:
            return False
    else:
        return False



def new_game():
    print('Добро пожаловать в числовую угадайку!')
    print('Здесь ты сможешь потренировать свою интуицию и логическое мышление. Чтобы начать, укажи максимум числового диапазона, в котором хочешь сыграть. Но не меньше единицы :)')
    global rand_number, err_count, n
    err_count = 0
    while True:
        n = input()
        if n.isdigit() and int(n) > 1:
            print('Отлично, начинаем! Попробуй угадать число от 1 до', n+'.', 'Количество попыток неограничено :)')
            rand_number = random.randint(1, int(n))
            break
        else:
            print('Максимумом диапазона может быть только целое число больше единицы. Попробуй еще раз.')

new_game()

while True:
    number = input()
    if is_valid(number) == False:
        print('Мы загадали для тебя только число от 1 до', n+',', 'ни больше, ни меньше :) Попробуй ещё раз.')
        continue
    else:
        if int(number) < rand_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            err_count += 1
        elif int(number) > rand_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            err_count += 1
        else:
            if err_count == 0:
                print('Ничего себе, вы угадали с первого раза! Поздравляем!')
            if err_count == 1:
                print('Совершенно верно! Вы угадали всего за 1 попытку, молодец!')
            if err_count in [2, 3, 4]:
                print('Совершенно верно!', 'Вы угадали за', err_count, 'попытки.')
            if err_count in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
                print('Совершенно верно!', 'Вы угадали за', err_count, 'попыток.')
            print('Сыграем еще раз? :) (да/нет)')
            answer = input()
            if answer == 'да':
                new_game()
            else:
                print('Спасибо, что сыграли в числовую угадайку. Приходите ещё! :)')
                break
