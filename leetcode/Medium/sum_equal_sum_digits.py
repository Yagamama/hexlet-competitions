# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/

# You are given a 0-indexed array nums consisting of positive integers. 
# You can choose two indices i and j, such that i != j, and the sum of 
# digits of the number nums[i] is equal to that of nums[j].

# Return the maximum value of nums[i] + nums[j] that you can obtain over 
# all possible indices i and j that satisfy the conditions.

# Example 1:

# Input: nums = [18,43,36,13,7]
# Output: 54
# Explanation: The pairs (i, j) that satisfy the conditions are:
# - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
# - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
# So the maximum sum that we can obtain is 54.

# Example 2:

# Input: nums = [10,12,19,14]
# Output: -1
# Explanation: There are no two numbers that satisfy the conditions, so we return -1.
 
# Constraints:
# 1 <= nums.length <= 10**5
# 1 <= nums[i] <= 10**9

# Hint 1
# What is the largest possible sum of digits a number can have?
# Hint 2
# Group the array elements by the sum of their digits, and 
# find the largest two elements of each group.

import heapq

def maximumSum(nums):
    digits = {}
    for num in nums:
        n = num
        s = 0
        while n > 0:
            s += n % 10
            n = n // 10
        if digits.get(s):
            heapq.heappush(digits[s], -num)
        else:
            digits[s] = [-num]
            heapq.heapify(digits[s])
        # print(digits)
    max_s = -1
    for d in digits.values():
        a = -heapq.heappop(d)
        if len(d) < 1:
            continue
        b = -heapq.heappop(d)
        max_s = max(max_s, a + b)
    return max_s


if __name__ == '__main__':
    print(maximumSum([18,43,36,13,7]))  # 54
    print(maximumSum([10,12,19,14]))  # -1
    print(maximumSum([4,6,10,6]))  # 12
