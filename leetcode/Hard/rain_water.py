# https://leetcode.com/problems/trapping-rain-water/description/

# Given n non-negative integers representing an elevation map where the 
# width of each bar is 1, compute how much water it can trap after raining.

# Example 1:

# 3                 x  
# 2         x ≈ ≈ ≈ x x ≈ x        x is elevation map
# 1     x ≈ x x ≈ x x x x x x      ≈ is water  
#    -------------------------
#     0 1 0 2 1 0 1 3 2 1 2 1   

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by 
# array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) 
# are being trapped.

# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

def trap(height):
    left = 0
    right = len(height) - 1
    water = 0
    i = 0
    while left < right:
        while height[left] <= i and left < right:
            left += 1
        while height[right] <= i and left < right:
            right -=1
        water = water + right - left + 1
        i += 1
    return water - sum(height) + height[left] - i


if __name__ == '__main__':
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
    print(trap([4,2,0,3,2,5]))  # 9
    print(trap([2,0,2]))  # 2
