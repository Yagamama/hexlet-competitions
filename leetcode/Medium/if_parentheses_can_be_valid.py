# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/

# A parentheses string is a non-empty string consisting only of '(' and ')'. 
# It is valid if any of the following conditions is true:

# It is ().
# It can be written as AB (A concatenated with B), where A and B are 
# valid parentheses strings.
# It can be written as (A), where A is a valid parentheses string.
# You are given a parentheses string s and a string locked, both of 
# length n. locked is a binary string consisting only of '0's and '1's. 
# For each index i of locked,

# If locked[i] is '1', you cannot change s[i].
# But if locked[i] is '0', you can change s[i] to either '(' or ')'.
# Return true if you can make s a valid parentheses string. 
# Otherwise, return false.

# Example 1:

# Input: s = "))()))", locked = "010100"
# Output: true
# Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
# We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.

# Example 2:

# Input: s = "()()", locked = "0000"
# Output: true
# Explanation: We do not need to make any changes because s is already valid.

# Example 3:

# Input: s = ")", locked = "0"
# Output: false
# Explanation: locked permits us to change s[0]. 
# Changing s[0] to either '(' or ')' will not make s valid.
 
# Constraints:

# n == s.length == locked.length
# 1 <= n <= 10**5
# s[i] is either '(' or ')'.
# locked[i] is either '0' or '1'.

def canBeValid(s='', locked=''):
    n = len(s)
    if n % 2:
        return False
    opened = []
    unlocked = []
    for i in range(n):
        if locked[i] == '0':
            unlocked.append(i)
            continue
        if s[i] == '(':
            opened.append(i)
        else:
            if opened:
                opened.pop()
            elif unlocked:
                unlocked.pop()
            else:
                return False
    while opened and unlocked and opened[-1] < unlocked[-1]:
        opened.pop()
        unlocked.pop()
    if opened:
        return False
    return True


if __name__ == '__main__':
    print(canBeValid("))()))", "010100"))  # true
    print(canBeValid("()()", "0000"))  # true
    print(canBeValid("())()))()(()(((())(()()))))((((()())(())", 
                     "1011101100010001001011000000110010100101"))  # true
                #    "(_)()_)(___)___(__(_)(______((__)_)__(_)"))  # true
    print(canBeValid(")", "0"))  # false
    print(canBeValid("())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(", 
                     "100011110110011011010111100111011101111110000101001101001111"))  # false
                #    "(___()((_((__()_))_(_)(((__(()_))(_()))))____(_(__))_(__)))("))  # false
