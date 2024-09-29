# https://leetcode.com/problems/valid-parentheses/description/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

# Example 4:

# Input: s = "([])"
# Output: true

def isValid(s):
    new_s=""
    while new_s != s:
        new_s = s
        s = s.replace("{}", "")
        s = s.replace("[]", "")
        s = s.replace("()", "")
    return len(s) == 0

print(isValid("()"))  # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))  # False
print(isValid("([])"))  # True
print(isValid("([]){[][(()[])]}"))  # True
print(isValid("([]){[]{[}(()[])]}"))  # False
