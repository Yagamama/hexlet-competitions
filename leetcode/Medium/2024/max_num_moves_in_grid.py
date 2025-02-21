# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/description/

# You are given a 0-indexed m x n matrix grid consisting of positive integers.

# You can start at any cell in the first column of the matrix, and 
# traverse the grid in the following way:

# From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), 
# (row, col + 1) and (row + 1, col + 1) such that the value of the cell you 
# move to, should be strictly bigger than the value of the current cell.
# Return the maximum number of moves that you can perform.

# Example 1:

#         2*  4*  3   5
#         5   4   9*  3
#         3   4   2   11*
#         10  9   13  15

# Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
# Output: 3
# Explanation: We can start at the cell (0, 0) and make the following moves:
# - (0, 0) -> (0, 1).
# - (0, 1) -> (1, 2).
# - (1, 2) -> (2, 3).
# It can be shown that it is the maximum number of moves that can be made.
# Example 2:

#         3   2   4
#         2   1   9
#         1   1   7

# Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
# Output: 0
# Explanation: Starting from any cell in the first column we cannot perform any moves.

def maxMoves(grid):
    moves = 0
    m = len(grid)
    n = len(grid[0])
    dct = {}

    def find_move(i=0, j=0, last=0):
        nonlocal moves, m, n, grid, dct
        if j == n or i in [-1, m]:
            return
        if (last >= grid[i][j]) or ((i, j) in dct):
            return
        moves = max(moves, j)
        dct[(i, j)] = moves
        find_move(i-1, j+1, grid[i][j])
        find_move(i, j+1, grid[i][j])
        find_move(i+1, j+1, grid[i][j])
    
    for i in range(m):
        find_move(i-1, 1, grid[i][0])
        find_move(i, 1, grid[i][0])
        find_move(i+1, 1, grid[i][0])
    return moves


if __name__ == '__main__':
    print(maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))  # 3
    print(maxMoves([[3,2,4],[2,1,9],[1,1,7]]))  # 0
