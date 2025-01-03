# https://leetcode.com/problems/search-insert-position/description/

# Given a sorted array of distinct integers and a target value, return the index if the 
# target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

def searchInsert(nums, target):
    min_idx = 0
    max_idx = len(nums) - 1
    if target < nums [min_idx]:
        return 0
    if target > nums[max_idx]:
        return len(nums)
    while True:
        center = (min_idx + max_idx) // 2
        if nums[center] == target:
            return center
        if max_idx - min_idx == 1:
            return max_idx
        if target > nums[center]:
            min_idx = center
        else:
            max_idx = center


if __name__ == '__main__':
    print(searchInsert([1,3,5,6], 5))  # 2
    print(searchInsert([1,3,5,6], 2))  # 1
    print(searchInsert([1,3,5,6], 7))  # 4
