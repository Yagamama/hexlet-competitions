# https://leetcode.com/problems/sort-colors/description/

# Given an array nums with n objects colored red, white, or blue, 
# sort them in-place so that objects of the same color are adjacent, 
# with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, 
# white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 
# Follow up: Could you come up with a one-pass algorithm using only 
# constant extra space?

# Hint 1
# A rather straight forward solution is a two-pass algorithm using counting sort.
# Hint 2
# Iterate the array counting number of 0's, 1's, and 2's.
# Hint 3
# Overwrite array with the total number of 0's, then 1's and followed by 2's.

def sortColors(nums) -> None:
    red, white, blue = 0, 0, 0
    for n in nums:
        if n == 0:
            red += 1
        elif n == 1:
            white += 1
        else:
            blue += 1
    nums[:red] = [0] * red
    nums[red:red+white] = [1] * white
    nums[red+white:] = [2] * blue
    print(nums)
    """
    Do not return anything, modify nums in-place instead.
    """

if __name__ == '__main__':
    sortColors([2,0,2,1,1,0])  # [0,0,1,1,2,2]
    sortColors([2,0,1])  # [0,1,2]
