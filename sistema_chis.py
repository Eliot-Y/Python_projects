def to_base_10(chislo, base_chislo):
    if base_chislo == 10:
        return int(chislo)
    lenggh = len(chislo)
    total = 0

    for i in range(lenggh):
        if chislo[-1] in '1234567890':
            total += int(chislo[-1]) * base_chislo ** i
        else:
            total += (ord(chislo[-1]) - 55) * base_chislo ** i
        chislo = chislo[:-1]
    return total


def to_new_base(chislo, base_chislo):
    total = ''
    temp = 0

    while chislo >= base_chislo:
        temp = int(chislo % base_chislo)
        if base_chislo > 10 and temp > 9:
            temp = chr(temp + 55)
            total += temp
        else:
            total += str(temp)
        chislo //= base_chislo
    total += str(chislo)
    return total[::-1]


number = input('Введите число >>> ')
old_base_number = int(input('Введите старое основание числа >>> '))
new_base_number = int(input('Введите новое основание числа >>> '))
number = to_base_10(number, old_base_number)
number = to_new_base(number, new_base_number)

print(number)
