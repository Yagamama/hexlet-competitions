# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Given a string s, find the length of the longest substring 
# without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence 
# and not a substring.
 
# Constraints:
# 0 <= s.length <= 5 * 10**4
# s consists of English letters, digits, symbols and spaces.

def lengthOfLongestSubstring(s):
    longest = 0
    chars = set()
    left = 0
    for i, c in enumerate(s):
        if c not in chars:
            longest = max(longest, i - left + 1)
            chars.add(c)
        else:
            for j in range(left, i):
                if s[j] == c:
                    left = j + 1
                    break
                chars.remove(s[j])
    return longest


if __name__ == '__main__':
    print(lengthOfLongestSubstring("abcabcbb"))  # 3
    print(lengthOfLongestSubstring("bbbbb"))  # 1
    print(lengthOfLongestSubstring("pwwkew"))  # 3
