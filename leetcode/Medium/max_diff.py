# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/description/

# You are given an integer num. You will apply the following steps 
# to num two separate times:

# Pick a digit x (0 <= x <= 9).
# Pick another digit y (0 <= y <= 9). Note y can be equal to x.
# Replace all the occurrences of x in the decimal representation of num by y.
# Let a and b be the two results from applying the operation to num independently.

# Return the max difference between a and b.
# Note that neither a nor b may have any leading zeros, and must not be 0.

# Example 1:

# Input: num = 555
# Output: 888
# Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
# The second time pick x = 5 and y = 1 and store the new integer in b.
# We have now a = 999 and b = 111 and max difference = 888

# Example 2:

# Input: num = 9
# Output: 8
# Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
# The second time pick x = 9 and y = 1 and store the new integer in b.
# We have now a = 9 and b = 1 and max difference = 8
 
# Constraints:
# 1 <= num <= 10**8

def maxDiff(num):
    maxn, minn = num, num
    snum = str(num)
    i = 0
    while i < len(snum) and snum[i] == '9':
        i += 1
    if i < len(snum):
        maxn = int(snum.replace(snum[i], '9', -1))
    i = 0
    # print(f'snum = {snum}')
    # snum = str(num)
    while i < len(snum) and snum[i] in ['1', '0']:
        i += 1
    if i == 0:
        minn = int(snum.replace(snum[0], '1', -1))
    elif i < len(snum):
        minn = int(snum.replace(snum[i], '0', -1))
    else: 
        minn = int(snum.replace(snum[0], '1', -1))
    print(f'num: {num}, max: {maxn}, min: {minn}')
    return maxn - minn


if __name__ == '__main__':
    print(maxDiff(555))  # 888
    # print(maxDiff(9))  # 8
    # print(maxDiff(9288))  # 8700
    # print(maxDiff(123456))  # 820000
    # print(maxDiff(111))  # 888
    # print(maxDiff(999))  # 888
    print(maxDiff(1101057))  # 8808050
