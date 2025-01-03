# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


def findMedianSortedArrays(nums1, nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    arr_len = l1 + l2
    i, j = 0, 0
    a, b, k = 0, 0, 0
    l = arr_len // 2
    while k <= l:
        if i == l1:
            a, b = b, nums2[j]
            j += 1
        elif j == l2:
            a, b = b, nums1[i]
            i += 1
        elif (nums1[i] < nums2[j]):
            a, b = b, nums1[i]
            i += 1
        else:
            a, b = b, nums2[j]
            j += 1
        # print(f'a = {a}, b = {b}')
        k += 1
    if arr_len % 2 == 0:
        median = (a + b) / 2
    else:
        median = b
    return median


if __name__ == '__main__':
    print(findMedianSortedArrays([1,3], [2]))  # 2
    print(findMedianSortedArrays([1,2,4], [3,5]))  # 3
    print(findMedianSortedArrays([5,6,7], [1,2]))  # 5
    print(findMedianSortedArrays([1,2], [6,7,8]))  # 6

    print(findMedianSortedArrays([1,2,4], [3,5,6]))  # 3,5
    print(findMedianSortedArrays([1,2,4,6,8], [3,5,6]))  # 4,5
