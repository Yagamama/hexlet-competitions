def romanToInt(s):
    rti = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    result = 0
    numb = [rti[x] for x in s]
    for i in range(len(numb)-1):
        if numb[i] < numb[i+1]:
            result -= numb[i]
        else:
            result += numb[i]
    result += numb[len(numb)-1]
    return result


if __name__ == '__main__':
    print(romanToInt('XXX'))
    print(romanToInt('LVIII'))
    print(romanToInt('MCMXCIV'))
    print(romanToInt('XIX'))