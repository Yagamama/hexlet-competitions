# https://leetcode.com/problems/best-sightseeing-pair/

# You are given an integer array values where values[i] represents 
# the value of the ith sightseeing spot. Two sightseeing spots i 
# and j have a distance j - i between them.

# The score of a pair (i < j) of sightseeing spots is 
# values[i] + values[j] + i - j: the sum of the values of the 
# sightseeing spots, minus the distance between them.

# Return the maximum score of a pair of sightseeing spots.

# Example 1:
# Input: values = [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

# Example 2:
# Input: values = [1,2]
# Output: 2

# Constraints:
# 2 <= values.length <= 5 * 10**4
# 1 <= values[i] <= 1000

def maxScoreSightseeingPair(values=[]):
    n = len(values)
    maxleft = values[0]
    score = 0
    for i in range(1, n):
        right = values[i] - i
        score = max(score, maxleft + right)
        left = values[i] + i
        maxleft = max(maxleft, left)
    return score


if __name__ == '__main__':
    print(maxScoreSightseeingPair([8,1,5,2,6]))  # 11
    print(maxScoreSightseeingPair([1,2]))  # 2
    print(maxScoreSightseeingPair([2,2,2]))  # 3
