# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description/

# In a row of dominoes, tops[i] and bottoms[i] represent the top and 
# bottom halves of the ith domino. (A domino is a tile with two numbers 
# from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

# Return the minimum number of rotations so that all the values in 
# tops are the same, or all the values in bottoms are the same.

# If it cannot be done, return -1.

# Example 1:
# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by tops and bottoms: 
# before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in 
# the top row equal to 2, as indicated by the second figure.

# Example 2:
# Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make 
# one row of values equal.
 
# Constraints:
# 2 <= tops.length <= 2 * 10**4
# bottoms.length == tops.length
# 1 <= tops[i], bottoms[i] <= 6

def minDominoRotations(tops, bottoms):
    val = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    l = len(tops)
    rotate = 0
    for i in range(l):
        val[tops[i]] = val.get(tops[i]) + 1
        if tops[i] != bottoms[i]:
            val[bottoms[i]] = val.get(bottoms[i]) + 1
        if val[tops[i]] == l:
            rotate = tops[i]
        if val[bottoms[i]] == l:
            rotate = bottoms[i]
    if not rotate:
        return -1
    c = tops.count(rotate)
    res = min(c, l-c)
    c = bottoms.count(rotate)
    res = min(c, res, l-c)
    return res


if __name__ == '__main__':
    print(minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))  # 2
    print(minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))  # -1
    print(minDominoRotations([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2]))  # 1
    print(minDominoRotations([2,1,1,1,2,2,2,1,1,2], [1,1,2,1,1,1,1,2,1,1]))  # 2
