# https://leetcode.com/problems/permutation-in-string/description/

# Given two strings s1 and s2, return true if s2 contains a permutation
# of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# Constraints:
# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

def checkInclusion(s1, s2):
    letters_s1 = sorted(s1.strip())
    lens1 = len(s1)
    for i in range(len(s2) - lens1 + 1):
        if s2[i] in letters_s1:
            if sorted(s2[i:i+lens1]) == letters_s1:
                return True
    return False

if __name__ == '__main__':
    print(checkInclusion("ab", "eidbaooo"))  # True
    print(checkInclusion("ab", "eidboaoo"))  # False
