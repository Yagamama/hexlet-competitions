# https://leetcode.com/problems/count-and-say/description/

# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Run-length encoding (RLE) is a string compression method that works by replacing 
# consecutive identical characters (repeated 2 or more times) with the concatenation 
# of the character and the number marking the count of the characters (length of the run). 
# For example, to compress the string "3322251" we replace "33" with "23", replace "222" 
# with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed 
# string becomes "23321511".

# Given a positive integer n, return the nth element of the count-and-say sequence.

# Example 1:

# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"

# Example 2:

# Input: n = 1
# Output: "1"
# Explanation: This is the base case.

def countAndSay(n):
    if n == 1:
        return '1'
    # print(f'---- {n} ----')
    result = '1'
    for _ in range(1, n):
        grps = []
        j = 0
        s = result[0]
        for j in range(len(result)-1):
            if result[j+1] == result[j]:
                s += result[j+1]
            else:
                grps.append(str(len(s))+s[0])
                s = result[j+1]
        grps.append(str(len(s))+s[0])
        result = ''.join(grps)
        # print(f'groups: {grps}')
        # print(result)
    return result

if __name__ == '__main__':
    print(countAndSay(1))  # 1
    print(countAndSay(2))  # 11
    print(countAndSay(3))  # 21
    print(countAndSay(4))  # 1211
    print(countAndSay(5))  # 111221
    print(countAndSay(6))  # 312211
