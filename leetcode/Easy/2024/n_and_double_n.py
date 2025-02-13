# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/

# Given an array arr of integers, check if there exist two indices i and j such that :
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# Example 1:

# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

# Example 2:

# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.

# Constraints:
# 2 <= arr.length <= 500
# -10**3 <= arr[i] <= 10**3

def checkIfExist(arr=[]):
    nums = set()
    for item in arr:
        if item * 2 in nums or item / 2 in nums:
            return True
        nums.add(item)
    return False


if __name__ == '__main__':
    print(checkIfExist([10,2,5,3]))  # true
    print(checkIfExist([5,2,10,3]))  # true
    print(checkIfExist([3,1,7,11]))  # false
