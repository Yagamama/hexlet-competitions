# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/

# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

# Example 1:

# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.

# Example 2:

# Input: matrix = 
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation: 
# There are 6 squares of side 1.  
# There is 1 square of side 2. 
# Total number of squares = 6 + 1 = 7.
 
# Constraints:
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1

def countSquares(matrix):
    res = 0
    m = len(matrix)
    n = len(matrix[0])
    min_val = min(m, n)
    for i in range(m):
        for j in range(n):
            if not matrix[i][j]:
                continue
            for k in range(0, min_val):
                s = sum([sum([x for x in z[j:j+k+1]]) for z in matrix[i:i+k+1]])
                if s == pow(k+1, 2):
                    res += 1
                    # print(f'i: {i}, j: {j}, k: {k}, sum: {s}')
                else:
                    break
    return res


if __name__ == '__main__':
    a = [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
        ]  # 15
    b = [
        [1,0,1],
        [1,1,0],
        [1,1,0]]  # 7
    print(countSquares(a))
    print(countSquares(b))
