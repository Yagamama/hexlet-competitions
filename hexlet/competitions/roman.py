import re


def to_roman(num):
    roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    res = ''
    i = 1  # разряд числа. Начинаем вычислять с последнего разряда
    while num > 0:
        digit = num % 10
        match digit:
            case 1 | 5:
                res = roman[digit * i] + res
            case 2 | 3:
                res = (roman[i]) * digit + res
            case 4:
                res = roman[i] + roman[i * 5] + res
            case 6 | 7 | 8:
                res = (roman[5 * i]) + roman[i] * (digit - 5) + res
            case 9:
                res = roman[i] + roman[i * 10] + res
        num = num // 10
        i = i * 10
    print(res)


def to_arabic(arab):
    arabian = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    str = re.findall('M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})', arab)
    str = re.findall('C', arab)
    print (str)
    order = {'V': 'I', 
             'X': 'I', 
             'L': 'X',
             'C': 'X',
             'D': 'C',
             'M': 'C',}
    res = 0
    if len(arab) > 3:  # Проверка, чтобы не было идущих 4х одинаковых символов подряд
        for i in range(len(arab)-3):
            four = arab[i:i+4]
            if four[0] == four[1] == four[2] == four[3]:
                return False
    for i in range(len(arab)-1):  # сравниваем посимвольно со следующим символом
        if arab[i] in arabian:
            if arabian[arab[i]] < arabian[arab[i+1]]:
                #if order[arab[i+1]] != arab[i]:
                #    print (f'order[arab[i+1]] = {order[arab[i+1]]}, arab[i] = {arab[i]}')
                #    return False
                res = res - arabian[arab[i]]
            else:
                res = res + arabian[arab[i]]
        else:
            return False
    if arab[len(arab)-1] in arabian:  # добавляем последний символ
        res = res + arabian[arab[len(arab)-1]]
    else:
        return False
    print(res)


if __name__ == '__main__':
    to_roman(1009)
    to_arabic('CDCCCXLVII')
