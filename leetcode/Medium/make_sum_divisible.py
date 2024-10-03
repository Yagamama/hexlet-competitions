# https://leetcode.com/problems/make-sum-divisible-by-p/description/

# Given an array of positive integers nums, remove the smallest subarray (possibly empty) 
# such that the sum of the remaining elements is divisible by p. It is not allowed to remove 
# the whole array.

# Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

# A subarray is defined as a contiguous block of elements in the array.

# Example 1:

# Input: nums = [3,1,4,2], p = 6
# Output: 1
# Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the 
# subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

# Example 2:

# Input: nums = [6,3,5,2], p = 9
# Output: 2
# Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is 
# to remove the subarray [5,2], leaving us with [6,3] with sum 9.

# Example 3:

# Input: nums = [1,2,3], p = 3
# Output: 0
# Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need 
# to remove anything.
 
# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= p <= 109

def minSubarray(nums, p) -> int:
    arr_sum = sum(nums)
    diff = arr_sum % p
    if diff == 0:
        return 0
    mods = [x % p for x in nums if x % p > 0]
    if diff in mods:
        return 1
    l_mods = len(mods)
    min_len = l_mods
    mods = {0: -1}
    cur_sum = 0
    for i in range (l_mods):
        cur_sum = (cur_sum + nums[i]) %p
        n = (cur_sum - diff + p) % p
        if n in mods:
            min_len = min(min_len, i - mods[n])
        mods[cur_sum] = i
    return min_len if min_len < l_mods else -1


if __name__ == '__main__':
    print(minSubarray([3,1,4,2], p = 6))  # 1
    print(minSubarray([6,3,5,2], p = 9))  #2
    print(minSubarray([6,1], p = 9))  #-1
    print(minSubarray([1,2,3], p = 3))  # 0
    print(minSubarray([17,3,16,12,3,19,1,8,5,8], p = 54))  # -1
    print(minSubarray([19,25,39,31,20,10,40,38,28,35,11,11,18,26,26,24,29,14,10,37], p = 23))  # 1
    print(minSubarray([3,7,14,15,7,16,27,7,9,21,1,17,25,31,30,28,22], p = 59))  # 4
    print(minSubarray([2,16,16,10,10,6,4,1,8,19], p = 36))  #2
