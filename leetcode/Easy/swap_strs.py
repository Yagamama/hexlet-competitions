# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

# You are given two strings s1 and s2 of equal length. A string swap is 
# an operation where you choose two indices in a string (not necessarily 
# different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing 
# at most one string swap on exactly one of the strings. Otherwise, return false.

# Example 1:

# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last 
# character of s2 to make "bank".

# Example 2:

# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.

# Example 3:

# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap 
# operation is required.
 
# Constraints:
# 1 <= s1.length, s2.length <= 100
# s1.length == s2.length
# s1 and s2 consist of only lowercase English letters.

def areAlmostEqual(s1, s2):
    if s1 == s2:
        return True
    a = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            a.append(i)
    if len(a) != 2:
        return False
    return s1[a[0]] == s2[a[1]] and s2[a[0]] == s1[a[1]]


if __name__ == '__main__':
    print(areAlmostEqual("bank", "kanb"))  # true
    print(areAlmostEqual("attack", "defend"))  # false
    print(areAlmostEqual("kelb", "kelb"))  # true
