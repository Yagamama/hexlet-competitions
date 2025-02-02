# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

# Given an array nums, return true if the array was originally sorted 
# in non-decreasing order, then rotated some number of positions 
# (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of 
# the same length such that A[i] == B[(i+x) % A.length], where % is 
# the modulo operation.

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the the 
# element of value 3: [3,4,5,1,2].

# Example 2:

# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.
# Example 3:

# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is the original sorted array.
# You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
 
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

def check(nums=[]):
    if not nums:
        return True
    minn = nums.index(min(nums))
    if minn == 0 and nums[-1] == nums[0]:
        minn = len(nums) - 1
        while minn > 0 and nums[minn - 1] == nums[minn]:
            minn -= 1
    return nums[minn:]+nums[:minn] == sorted(nums)


if __name__ == '__main__':
    print(check([3,4,5,1,2]))  # true
    print(check([2,1,3,4]))  # false
    print(check([1,2,3]))  # true
    print(check([6,10,6]))  # true
