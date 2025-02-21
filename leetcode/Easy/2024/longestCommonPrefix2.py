# https://leetcode.com/problems/longest-common-prefix/description/

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

def longestCommonPrefix(strs):
    if not strs:
        return ''
    s = min(strs, key=len)
    if len(s) == 0:
        return ''
    prefs = [s[:i+1] for i in range(len(s))]
    length = len(prefs)
    for pr in prefs[::-1]:
        for item in strs:
            if not item.startswith(pr):
                length -= 1
                if length == 0:
                    return ''
                break
    return prefs[length-1]


if __name__ == '__main__':
    print(longestCommonPrefix(["flower","flow","flight"]))  # fl
    print(longestCommonPrefix(["dog","racecar","car","bz"]))  # 
    print(longestCommonPrefix(["reflower","flow","flight"]))  # 
    print(longestCommonPrefix(["cir","car"]))  # c
    print(longestCommonPrefix([""]))  # 
