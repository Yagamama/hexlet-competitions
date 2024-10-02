# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/

# Given an array of integers arr of even length n and an integer k.

# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

# Return true If you can find a way to do that or false otherwise.

# Example 1:

# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

# Example 2:

# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).

# Example 3:

# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to divide arr 
# into 3 pairs each with sum divisible by 10.


def canArrange(arr, k):
    arr2 = sorted([x % k for x in arr if x % k > 0])
    if len(arr2) % 2 != 0:
        return False
    while len(arr2) > 0:
        if (arr2[0] + arr2[len(arr2)-1]) % k == 0:
            arr2.pop(len(arr2)-1)
            arr2.pop(0)
        else:
            return False
    return True



if __name__ == '__main__':
    print(canArrange([1,2,3,4,5,10,6,7,8,9], 5))  # True
    print(canArrange([1,2,3,4,5,6], 7))  # True
    print(canArrange([1,2,3,4,5,6], 10))  # False
    print(canArrange([2,3,7,-9,4,4,7,3,2,10,8,15,2,1,-8,10,-5,10,-2,21,9,20,0,4,24,5,12,-10,8,9,18,13,
                      -8,10,-4,-3,0,16,-4,8,14,15,-9,0,0,-6,11,-3,10,11,7,-1,-5,5,11,2,5,9,-2,8,9,-10,6,
                      -2,7,8,3,0,-2,11], 18))  # True
