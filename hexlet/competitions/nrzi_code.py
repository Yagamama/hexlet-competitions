def decode(code):
    a = '0'
    result = ''
    for symbol in code:
        if symbol == '|':
            a = '1'
        else:
            result += a
            a = '0'
    print(result)
    return result


if __name__ == '__main__':
    decode('_|¯|____|¯|__|¯¯¯')
    #      '0 1 1000 1 10 100'
    decode('|¯|___|¯¯¯¯¯|___|¯|_|¯')
    #      ' 1 100 10000 100 1 1 1'
    decode('¯|___|¯¯¯¯¯|___|¯|_|¯')
    #      '0 100 10000 100 1 1 1'