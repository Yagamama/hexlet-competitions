# https://leetcode.com/problems/integer-to-roman/description/

def intToRoman(num):
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
    return res


if __name__ == '__main__':
    print(intToRoman(3749))  # MMMDCCXLIX
    print(intToRoman(58))  # LVIII
    print(intToRoman(1994))  # MCMXCIV
    