from random import *


def chars_of_pass():  # Возвращает все символы, которые будут использоваться в генерации
    print("Да - \"д\", нет - \"н\"")
    chars_temp = ''
    flag1 = input('Включать ли цифры 0123456789? ')
    flag2 = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ')
    flag3 = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ')
    flag4 = input('Включать ли символы !#$%&*+-=?@^_? ')
    flag5 = input('Исключать ли неоднозначные символы il1Lo0O? ')
    if flag1 == 'д':
        chars_temp += '0123456789'
    if flag2 == 'д':
        chars_temp += 'abcdefghijklmnopqrstuvwxyz'
    if flag3 == 'д':
        chars_temp += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if flag4 == 'д':
        chars_temp += '!#$%&*+-=?@^_?'
    if flag5 == 'д':
        chars_temp_list = []
        chars_temp_list.extend(chars_temp)
        i = 0
        while i < len(chars_temp_list):
            if chars_temp_list[i] in 'il1Lo0O':
                del chars_temp_list[i]
            else:
                i += 1
        chars_temp = ''.join(chars_temp_list)
    return chars_temp


def generate_password(len_pass, chars):
    return ''.join(sample(chars, len_pass))


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
amount_pass = int(input('Введите колличество паролей: '))
len_pass = int(input('Введите длину паролей: '))

chars = chars_of_pass()
print("Список паролей:")
for i in range(amount_pass):
    print(f'{i + 1}. {generate_password(len_pass, chars)}')
