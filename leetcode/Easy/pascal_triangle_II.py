# https://leetcode.com/problems/pascals-triangle-ii/description/

# Given an integer rowIndex, return the rowIndexth (0-indexed) 
# row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two 
# numbers directly above it as shown:

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:

# Input: rowIndex = 0
# Output: [1]

# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 
# Constraints:
# 0 <= rowIndex <= 33

def getRow(rowIndex):
    triangle = [[1]]
    for i in range(1, rowIndex+1):
        line = [1]
        for j in range(1, i+1):
            if j < i:
                line.append(triangle[i-1][j-1] + triangle[i-1][j])
            else:
                line.append(1)
        triangle.append(line)
    return triangle[-1]


if __name__ == '__main__':
    print(getRow(3))  # [1,3,3,1]
    print(getRow(0))  # [1]
    print(getRow(1))  # [1,1]
