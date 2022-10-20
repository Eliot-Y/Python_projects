def get_list_words(first_str):  # Преобраует строку в лист со словами
    for c in first_str:
        if not c.isalpha() and c != ' ':
            first_str = first_str.replace(c, '', 1)
    return first_str.split()


def get_encrypt_char(old_char, sdv_step):    # Принимает символ и длину слова ///  возвращает его зашифрованым
    eng_alp = 'abcdefghijklmnopqrstuvwxyz'
    if old_char.isupper():
        eng_alp = eng_alp.upper()
    index_old_char = eng_alp.find(old_char)
    new_char = eng_alp[(index_old_char + sdv_step) % 26]
    return new_char


def to_encrypt_list(list_wtf):    # Принимает лист слов /// возвращает лист зашифрованных слов
    new_word = ''
    for i in range(len(list_wtf)):
        for j in range(len(list_wtf[i])):
            new_word += get_encrypt_char(list_wtf[i][j], len(list_wtf[i]))
        list_wtf[i] = new_word
        new_word = ''
    return list_wtf


user_text = input()
list_user_words = get_list_words(user_text)    # ВЕЛИКА ЗАГАДКА ЛИСТА
list_che_bly = list_user_words.copy()    # буффер
encryption_list = to_encrypt_list(list_che_bly)

for i in range(len(list_user_words)):    # Меняем старые cлова в строке на новые
    user_text = user_text.replace(list_user_words[i], encryption_list[i], 1)

print(user_text)