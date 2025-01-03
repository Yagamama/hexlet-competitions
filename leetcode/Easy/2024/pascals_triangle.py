# https://leetcode.com/problems/pascals-triangle/description/

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

#             1
#           1   1
#         1   2   1
#       1   3   3   1
#     1   4   6   4   1

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:

# Input: numRows = 1
# Output: [[1]]

def generate(numRows):
    triangle = [[1]]
    for i in range(1, numRows):
        line = [1]
        for j in range(1, i+1):
            if j < i:
                line.append(triangle[i-1][j-1] + triangle[i-1][j])
            else:
                line.append(1)
        triangle.append(line)
    return triangle


if __name__ == '__main__':
    print(generate(5))  # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    print(generate(1))  # [[1]]
