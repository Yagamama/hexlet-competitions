# https://leetcode.com/problems/count-largest-group/description/

# You are given an integer n.
# Each number from 1 to n is grouped according to the sum of its digits.
# Return the number of groups that have the largest size.

# Example 1:

# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum 
# of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with largest size.

# Example 2:

# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.
 
# Constraints:
# 1 <= n <= 10**4

def countLargestGroup(n):
    res = 0
    grps = {}
    maxs = 0
    for num in range(1, n+1):
        s = 0
        while num > 0:
            s += num % 10
            num = num // 10
        grps[s] = grps.get(s, 0) + 1
        maxs = max(maxs, grps[s])
    for g in grps.values():
        res = res +1 if g == maxs else res
    return res


if __name__ == '__main__':
    print(countLargestGroup(13))  # 4
    print(countLargestGroup(2))  # 2
