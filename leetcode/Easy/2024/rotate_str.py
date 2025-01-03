# https://leetcode.com/problems/rotate-string/description/

# Given two strings s and goal, return true if and only if s can 
# become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to 
# the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.

# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true

# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false

# Constraints:
# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.

def rotateString(s='', goal=''):
    # start = s.find(goal[0])
    # while start >= 0:
    #     if goal == s[start:] + s[:start]:
    #         return True
    #     start = s.find(goal[0], start+1)
    # return False
    return goal in s + s

if __name__ == '__main__':
    print(rotateString("abcde", "cdeab"))  # True
    print(rotateString("abcde", "abced"))  # False
