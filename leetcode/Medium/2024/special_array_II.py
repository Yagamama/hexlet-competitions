# https://leetcode.com/problems/special-array-ii/description/

# An array is considered special if every pair of its adjacent elements 
# contains two numbers with different parity.

# You are given an array of integer nums and a 2D integer matrix 
# queries, where for queries[i] = [fromi, toi] your task is to check that 
# subarray nums[fromi..toi] is special or not.

# Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

# Example 1:
# Input: nums = [3,4,1,2,6], queries = [[0,4]]
# Output: [false]
# Explanation:
# The subarray is [3,4,1,2,6]. 2 and 6 are both even.

# Example 2:
# Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]
# Output: [false,true]
# Explanation:
# The subarray is [4,3,1]. 3 and 1 are both odd. So the answer 
# to this query is false.
# The subarray is [1,6]. There is only one pair: (1,6) and it 
# contains numbers with different parity. So the answer to this query is true.
 
# Constraints:
# 1 <= nums.length <= 10**5
# 1 <= nums[i] <= 10**5
# 1 <= queries.length <= 10**5
# queries[i].length == 2
# 0 <= queries[i][0] <= queries[i][1] <= nums.length - 1

def isArraySpecial(nums, queries):
    answer = []
    equals = [0]
    for i in range(1, len(nums)):
        equals.append(equals[i-1])
        if nums[i] % 2 == nums[i-1] % 2:
            equals[i] += 1
    for i in range(len(queries)):
        start, end = queries[i][0], queries[i][1]
        answer.append(True) if equals[end] - equals[start] == 0 else answer.append(False)
    return answer


if __name__ == '__main__':
    print(isArraySpecial([3,4,1,2,6], [[0,4]]))  # [false]
    print(isArraySpecial([4,3,1,6], [[0,2],[2,3]]))  # [false,true]