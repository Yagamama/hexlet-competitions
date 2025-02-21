# https://leetcode.com/problems/excel-sheet-column-number/description/

# Given a string columnTitle that represents the column title as appears in 
# an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...

# Example 1:
# Input: columnTitle = "A"
# Output: 1

# Example 2:
# Input: columnTitle = "AB"
# Output: 28

# Example 3:
# Input: columnTitle = "ZY"
# Output: 701
 

# Constraints:
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].

def titleToNumber(columnTitle=''):
    columnTitle = columnTitle[::-1]
    num = 0
    for i in range(len(columnTitle)):
        num += pow(26, i) * (ord(columnTitle[i]) - ord('A') + 1)
    return num


if __name__ == '__main__':
    print(titleToNumber("A"))  # 1
    print(titleToNumber("E"))  # 5
    print(titleToNumber("AB"))  # 28
    print(titleToNumber("ZY"))  # 701
    