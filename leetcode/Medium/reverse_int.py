# https://leetcode.com/problems/reverse-integer/description/

# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer 
# range [-2**31, 2**31 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321

# Example 2:

# Input: x = -123
# Output: -321

# Example 3:

# Input: x = 120
# Output: 21

def reverse(x: int) -> int:

    # variant 1:

    # max_range = pow(2, 31)   # 2_147_483_648
    # new_x = int(str(x)[-1:0:-1]) if x < 0 else int(str(x)[::-1])
    # if (new_x < -max_range) or (new_x > max_range - 1):
    #     return 0
    # return -new_x if x < 0 else new_x

    # variant 2:

    max_range = pow(2, 31)
    new_x = 0
    is_negative = x < 0
    x = abs(x)
    while x > 0:
        digit = x % 10
        if new_x * 10 + digit > max_range:
            return 0
        new_x = new_x * 10 + digit
        x = x // 10
    return -new_x if is_negative else new_x

if __name__ == '__main__':
    print(reverse(123))  # Output: 321
    print(reverse(-123))  # Output: -321
    print(reverse(120))  # Output: 21
    print(reverse(1_534_236_469))  # Output: 0
