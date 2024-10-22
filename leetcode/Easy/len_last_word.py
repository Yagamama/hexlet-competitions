# https://leetcode.com/problems/length-of-last-word/

# Given a string s consisting of words and spaces, return the length 
# of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
    
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
    
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

def lengthOfLastWord(s=''):
    s = s.strip()
    lst = s.split(' ')
    lst = [x for x in lst if x]
    return len(lst[-1])


if __name__ == '__main__':
    print(lengthOfLastWord("Hello World"))  # 5
    print(lengthOfLastWord("   fly me   to   the moon  "))  # 4
    print(lengthOfLastWord("luffy is still joyboy"))  # 6
