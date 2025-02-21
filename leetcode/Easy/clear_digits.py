# https://leetcode.com/problems/clear-digits/description/

# You are given a string s.
# Your task is to remove all digits by doing this operation repeatedly:
# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.

# Example 1:
# Input: s = "abc"
# Output: "abc"
# Explanation:
# There is no digit in the string.

# Example 2:
# Input: s = "cb34"
# Output: ""
# Explanation:
# First, we apply the operation on s[2], and s becomes "c4".
# Then we apply the operation on s[1], and s becomes "".

# Constraints:
# 1 <= s.length <= 100
# s consists only of lowercase English letters and digits.
# The input is generated such that it is possible to delete all digits.

# Hint 1
# Process string s from left to right, if s[i] is a digit, mark the 
# nearest unmarked non-digit index to its left.
# Hint 2
# Delete all digits and all marked characters.

def clearDigits(s):
    marks = []
    for i, char in enumerate(s):
        if char.isdigit(): 
            marks.append(1)
            k = i - 1
            while k >= 0:
                if marks[k] == 0:
                    marks[k] = 1
                    break
                else:
                    k -= 1
        else:
            marks.append(0)
    result = [s[i] for i in range(len(s)) if marks[i] == 0]
    return ''.join(result)


if __name__ == '__main__':
    print(clearDigits("abc"))  # "abc"
    print(clearDigits("cb34"))  # ""
