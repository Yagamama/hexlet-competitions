# https://leetcode.com/problems/rotate-image/description/

# You are given an n x n 2D matrix representing an image, rotate the 
# image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify 
# the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

#         1  2  3         7  4  1 
#         4  5  6   ->    8  5  2 
#         7  8  9         9  6  3

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:

#         5  1  9 11        15 13  2  5 
#         2  4  8 10   ->   14  3  4  1 
#        13  3  6  7        12  6  8  9
#        15 14 12 16        16  7 10 11

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

def rotate(matrix):
    n = len(matrix)
    for i in range(n // 2):
        matrix[i][i], matrix[i][n-i-1], matrix[n-i-1][n-i-1], matrix[n-i-1][i] = \
        matrix[n-i-1][i], matrix[i][i], matrix[i][n-i-1], matrix[n-i-1][n-i-1]
        for j in range(i+1, n-i-1):
            matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i] = \
            matrix[n-j-1][i], matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1]
            # print('----')
    for k in range(len(matrix)):
        print(matrix[k])
    return

if __name__ == '__main__':
    print(rotate([[1,2,3],[4,5,6],[7,8,9]]))  # [[7,4,1],[8,5,2],[9,6,3]]
    print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))  
    # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    print(rotate([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))  
