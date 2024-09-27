# https://leetcode.com/problems/integer-to-english-words/description/

# Convert a non-negative integer num to its English words representation.

 

# Example 1:

# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:

# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:

# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

# Constraints:
# 0 <= num <= 2**31 - 1


def numberToWords (num):
    bignums = {
        1: 'Thousand', 
        2: 'Million',  # 6 zero
        3: 'Billion',  # 9 zero
        4: 'Trillion',  # 12 zero
        # 5: 'Quadrillion',  # 15 zero
        # 6: 'Quintillion',  # 18 zero
        # 7: 'Sextillion',  # 21 zero
        # 8: 'Septillion',  # 24 zero
        # 9: 'Octillion',  # 27 zero
        # 10: 'Nonillion'  # 30 zero
    }

    ones = {
        1: 'One', 
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven', 
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
    }

    decades = {
        1: 'Ten', 
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy',
        8: 'Eighty',
        9: 'Ninety',
    }

    if num == 0:
        return 'Zero'
    thsnd = 0
    result = ''
    while num > 0:
        r = ''
        part = num % 1000
        hundreds = part // 100
        if hundreds:
            r = f"{ones[hundreds]} Hundred"
        part = part % 100
        if (part > 0) and (part < 20):
            r = f"{r} {ones[part]}"
        else:
            if part // 10:
                r = f"{r} {decades[part // 10]}"
            if part % 10:
                r = f"{r} {ones[part % 10]}"
        if thsnd and r:
            r = f"{r} {bignums[thsnd]}"
        num = num // 1000
        thsnd += 1
        if result:
            result = f"{r.strip()} {result.strip()}"
        else:
            result = r
    return result.strip()


if __name__ == '__main__':
    print(numberToWords(100))
    # print(numberToWords(123)) # One Hundred Twenty Three
    # print(numberToWords(12345)) # Twelve Thousand Three Hundred Forty Five
    # print(numberToWords(1234567)) # One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven
    # print(numberToWords(114)) # One Hundred Fourteen
    # print(numberToWords(12114765809)) # Twelve Billion One Hundred Fourteen Million Seven Hundred Sixty Five Thousand Eigth Hundred Nine
