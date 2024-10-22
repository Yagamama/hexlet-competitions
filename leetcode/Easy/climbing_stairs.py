# https://leetcode.com/problems/climbing-stairs/description/

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct 
# ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

def climbStairs(n):
    if n < 2:
        return n
    res = [1,1]
    for i in range(1,n):
        res.append(res[i]+res[i-1])
    return res[-1]

if __name__ == '__main__':
    print(climbStairs(2))  # 2
    print(climbStairs(3))  # 3
    print(climbStairs(4))  # 5
    