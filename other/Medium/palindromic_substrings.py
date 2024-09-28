# https://leetcode.com/problems/palindromic-substrings/description/

# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


def countSubstrings(s):
    result = 0 
    for i in range(len(s)):
        for j in range(i, len(s)):
            a = s[i:j+1]
            if a == a[::-1]:
                result +=1
    return result


if __name__ == '__main__':
    print(countSubstrings("abc"))  # 3
    print(countSubstrings("aaa"))  # 6
    