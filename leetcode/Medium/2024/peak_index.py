# https://leetcode.com/problems/peak-index-in-a-mountain-array/

# You are given an integer mountain array arr of length n where the 
# values increase to a peak element and then decrease.

# Return the index of the peak element.

# Your task is to solve it in O(log(n)) time complexity.

# Example 1:
# Input: arr = [0,1,0]
# Output: 1

# Example 2:
# Input: arr = [0,2,1,0]
# Output: 1

# Example 3:
# Input: arr = [0,10,5,2]
# Output: 1

# Constraints:
# 3 <= arr.length <= 10**5
# 0 <= arr[i] <= 10**6
# arr is guaranteed to be a mountain array.

def peakIndexInMountainArray(arr):
    left = 0
    right = len(arr)
    med = (right - left) // 2
    while arr[med+1] >= arr[med] or arr[med-1] >= arr[med]:
        if arr[med] <= arr[med-1]:
            right = med
        elif arr[med] <= arr[med+1]:
            left = med
        med = (right - left) // 2 + left
    return med


if __name__ == '__main__':
    print(peakIndexInMountainArray([0,1,0]))  # 1
    print(peakIndexInMountainArray([0,2,1,0]))  # 1
    print(peakIndexInMountainArray([0,5,10,5,2]))  # 2
    print(peakIndexInMountainArray([3,4,5,1]))  # 2
    print(peakIndexInMountainArray([0,1,2,3,4,5,7,10,2]))  # 7
    print(peakIndexInMountainArray([0,1,2,3,4,5,7,8,10,2]))  # 8
