# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/description/

# You are given an array nums consisting of positive integers.
# Starting with score = 0, apply the following algorithm:

# Choose the smallest integer of the array that is not marked. If there 
# is a tie, choose the one with the smallest index.
# Add the value of the chosen integer to score.
# Mark the chosen element and its two adjacent elements if they exist.
# Repeat until all the array elements are marked.
# Return the score you get after applying the above algorithm.

# Example 1:

# Input: nums = [2,1,3,4,5,2]
# Output: 7
# Explanation: We mark the elements as follows:
# - 1 is the smallest unmarked element, so we mark it and its 
# two adjacent elements: [2,1,3,4,5,2].
# - 2 is the smallest unmarked element, so we mark it and its 
# left adjacent element: [2,1,3,4,5,2].
# - 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
# Our score is 1 + 2 + 4 = 7.

# Example 2:

# Input: nums = [2,3,5,1,3,2]
# Output: 5
# Explanation: We mark the elements as follows:
# - 1 is the smallest unmarked element, so we mark it and its 
# two adjacent elements: [2,3,5,1,3,2].
# - 2 is the smallest unmarked element, since there are two 
# of them, we choose the left-most one, so we mark the one at 
# index 0 and its right adjacent element: [2,3,5,1,3,2].
# - 2 is the only remaining unmarked element, so we mark it: [2,3,5,1,3,2].
# Our score is 1 + 2 + 2 = 5.

# Constraints:
# 1 <= nums.length <= 10**5
# 1 <= nums[i] <= 10**6

import heapq

def findScore(nums=[]):
    score = 0
    marked = [False] * len(nums)
    heap = []
    for i in range(len(nums)):
        heapq.heappush(heap, (nums[i], i))

    while heap:
        n, index = heapq.heappop(heap)
        if not marked[index]:
            score += n
            marked[index] = True
            if index > 0:
                marked[index-1] = True
            if index < len(nums)-1:
                marked[index+1] = True
    return score


if __name__ == '__main__':
    print(findScore([2,1,3,4,5,2]))  # 7
    print(findScore([2,3,5,1,3,2]))  # 5
    print(findScore([10,44,10,8,48,30,17,38,41,27,16,33,45,45,34,30,22,3,42,42]))  # 212
