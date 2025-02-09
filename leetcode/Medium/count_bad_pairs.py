# https://leetcode.com/problems/count-number-of-bad-pairs/description/

# You are given a 0-indexed integer array nums. A pair of indices (i, j) 
# is a bad pair if i < j and j - i != nums[j] - nums[i].

# Return the total number of bad pairs in nums.

# Example 1:

# Input: nums = [4,1,3,3]
# Output: 5
# Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
# The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
# The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
# The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
# The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
# There are a total of 5 bad pairs, so we return 5.

# Example 2:

# Input: nums = [1,2,3,4,5]
# Output: 0
# Explanation: There are no bad pairs.
 
# Constraints:
# 1 <= nums.length <= 10**5
# 1 <= nums[i] <= 10**9

# Hint 1
# Would it be easier to count the number of pairs that are not bad pairs?
# Hint 2
# Notice that (j - i != nums[j] - nums[i]) is the same as 
# (nums[i] - i != nums[j] - j).
# Hint 3
# Keep a counter of nums[i] - i. To be efficient, use a HashMap.

def countBadPairs(nums):
    res = 0
    diff = {}
    pairs = 0
    for i, n in enumerate(nums):
        pairs += i
        num = n - i
        if diff.get(num):
            diff[num].append(i)
            res += len(diff[num]) - 1
        else:
            diff[num] = [i]
    return pairs - res

    # time limit:
    # res = 0
    # diff = {}
    # for i, n in enumerate(nums):
    #     diff[i] = n - i
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if diff[i] != diff[j]:
    #             res += 1
    # return res


if __name__ == '__main__':
    print(countBadPairs([4,1,3,3]))  # 5
    print(countBadPairs([1,2,3,4,5]))  # 0
