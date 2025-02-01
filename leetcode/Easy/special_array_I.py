# https://leetcode.com/problems/special-array-i/description/

# An array is considered special if every pair of its adjacent 
# elements contains two numbers with different parity.

# You are given an array of integers nums. Return true if nums 
# is a special array, otherwise, return false.

# Example 1:
# Input: nums = [1]
# Output: true
# Explanation:
# There is only one element. So the answer is true.

# Example 2:
# Input: nums = [2,1,4]
# Output: true
# Explanation:
# There is only two pairs: (2,1) and (1,4), and both of them contain 
# numbers with different parity. So the answer is true.

# Example 3:
# Input: nums = [4,3,1,6]
# Output: false
# Explanation:
# nums[1] and nums[2] are both odd. So the answer is false.

def isArraySpecial(nums=[]):
    if not nums:
        return True
    prev = nums[0] % 2
    for n in nums[1:]:
        if prev == n % 2:
            return False
        prev = n % 2
    return True


if __name__ == '__main__':
    print(isArraySpecial([1]))  # true
    print(isArraySpecial([2,1,4]))  # true
    print(isArraySpecial([4,3,1,6]))  # false
