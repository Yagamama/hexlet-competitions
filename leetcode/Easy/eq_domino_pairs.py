# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/

# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to 
# dominoes[j] = [c, d] if and only if either (a == c and b == d), or 
# (a == d and b == c) - that is, one domino can be rotated to be 
# equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, 
# and dominoes[i] is equivalent to dominoes[j].

# Example 1:
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1

# Example 2:
# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3
 
# Constraints:
# 1 <= dominoes.length <= 4 * 10**4
# dominoes[i].length == 2
# 1 <= dominoes[i][j] <= 9

def numEquivDominoPairs(dominoes):
    dom = {}
    for d in dominoes:
        a, b = min(d[0], d[1]), max(d[0], d[1])
        dom[(a, b)] = dom.get((a, b), 0) + 1
    print(dom)
    return sum((1+(x-1))*(x-1)//2 for x in dom.values() if x > 1)


if __name__ == '__main__':
    print(numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))  # 1
    print(numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))  # 3
    print(numEquivDominoPairs([[2,1],[1,2],[1,2],[1,2],[2,1],[1,1],[1,2],[2,2]]))  # 15
