def get_new_char(old_char, new_actual_alp, size_alp1):
    if old_char.isupper():
        new_actual_alp = new_actual_alp.upper()
    index_old_char = new_actual_alp.find(old_char)
    new_char = new_actual_alp[(index_old_char + sdvig) % size_alp1]
    return new_char


napravlenie_sdviga = input("Задайте направление сдвига\n1 - шифрование\n0 - дешифрование\n>>> ")
what_language = input('Введите название языка\n1 - en\n2 - ru\n>>> ')
sdvig = int(input('Задайте значение сдвига, 0 - неизвестно >>> '))
text_0, text_1 = input('Введите текст:\n'), ''

if napravlenie_sdviga == '0':
    sdvig = -sdvig

if what_language == '1':
    actual_alp = 'abcdefghijklmnopqrstuvwxyz'
    size_alp = 26
else:
    actual_alp = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    size_alp = 32

if sdvig == 0:
    for j in range(1, size_alp):
        sdvig += 1
        for i in range(len(text_0)):
            if not text_0[i].isalpha():
                text_1 += text_0[i]
                continue
            text_1 += get_new_char(text_0[i], actual_alp, size_alp)
        print(f'{j}. {text_1}')
        text_1 =''
else:
    for i in range(len(text_0)):
        if not text_0[i].isalpha():
            text_1 += text_0[i]
            continue
        text_1 += get_new_char(text_0[i], actual_alp, size_alp)

if text_1:
    print('Новая строка:\n', text_1, sep='')


