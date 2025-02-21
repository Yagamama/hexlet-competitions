# https://leetcode.com/problems/zigzag-conversion/

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 
# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"


def convert(s: str, numRows: int) -> str:
    i = 0
    k = 0
    rows = [[] for _ in range(numRows)]
    go_down = True
    while k < len(s):
        rows[i].append(s[k])
        k += 1
        if go_down:
            if numRows > 1:
                i += 1
                if i == numRows - 1:
                    go_down = False
        else:
            i -= 1
            if i == 0:
                go_down = True
    return ''.join([''.join(item) for item in rows])

if __name__ == '__main__':
    print(convert(s = "PAYPALISHIRING", numRows = 3))  # PAHNAPLSIIGYIR
    print(convert(s = "PAYPALISHIRING", numRows = 4))  # PINALSIGYAHRPI
    print(convert(s = "F", numRows = 1))  # F
    print(convert(s = "AB", numRows = 1))  # AB
