# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array nums​​​, return the minimum number of elements to 
# remove to make nums​​​ a mountain array.

# Example 1:

# Input: nums = [1,3,1]
# Output: 0
# Explanation: The array itself is a mountain array so we do not need to remove any elements.

# Example 2:

# Input: nums = [2,1,1,5,6,2,3,1]
# Output: 3
# Explanation: One solution is to remove the elements at indices 0, 1, and 5, 
# making the array nums = [1,5,6,3,1].
 
# Constraints:
# 3 <= nums.length <= 1000
# 1 <= nums[i] <= 109
# It is guaranteed that you can make a mountain array out of nums.

def minimumMountainRemovals(nums=[]):
    count = 0
    n = len(nums)
    incr = [1] * n
    decr = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                incr[i] = max(incr[i], incr[j] + 1)
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                decr[i] = max(decr[i], decr[j] + 1)
    # print(f'incr: {incr}\ndecr: {decr}')
    for i in range(1, n-1):
        if incr[i] > 1 and decr[i] > 1:
            count = max(count, incr[i] + decr[i] - 1)
    return n - count


if __name__ == '__main__':
    print(minimumMountainRemovals([1,3,1]))  # 0
    print(minimumMountainRemovals([2,1,1,5,6,2,3,1]))  # 3
    print(minimumMountainRemovals([9,8,1,7,6,5,4,3,2,1]))  # 2
    print(minimumMountainRemovals([23,47,63,72,81,99,88,55,21,33,32]))  # 1
