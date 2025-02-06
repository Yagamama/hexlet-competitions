# https://leetcode.com/problems/tuple-with-same-product/description/

# Given an array nums of distinct positive integers, return the number 
# of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are 
# elements of nums, and a != b != c != d.

# Example 1:

# Input: nums = [2,3,4,6]
# Output: 8
# Explanation: There are 8 valid tuples:
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

# Example 2:

# Input: nums = [1,2,4,5,10]
# Output: 16
# Explanation: There are 16 valid tuples:
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 
# Constraints:
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10**4
# All elements in nums are distinct.

def tupleSameProduct(nums):
    freq = {}
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            p = nums[i] * nums[j]
            freq[p] = freq.get(p, 0) + 1
    s = 0
    for n in freq.values():
        if n > 1:
            s += 8 * ((n - 1) * n // 2)
    return s


if __name__ == '__main__':
    print(tupleSameProduct([2,3,4,6]))  # 8
    print(tupleSameProduct([1,2,4,5,10]))  # 16
    print(tupleSameProduct([2,3,4,6,8,12]))  # 40
    print(tupleSameProduct([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]))  # 1288
