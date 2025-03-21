# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/

# You are given the root of a binary tree and a positive integer k.
# The level sum in the tree is the sum of the values of the nodes 
# that are on the same level.
# Return the kth largest level sum in the tree (not necessarily distinct). 
# If there are fewer than k levels in the tree, return -1.
# Note that two nodes are on the same level if they have the same 
# distance from the root.

# Example 1:

#             5
#         8       9
#     2   1       3   7
#   4   6

# Input: root = [5,8,9,2,1,3,7,4,6], k = 2
# Output: 13
# Explanation: The level sums are the following:
# - Level 1: 5.
# - Level 2: 8 + 9 = 17.
# - Level 3: 2 + 1 + 3 + 7 = 13.
# - Level 4: 4 + 6 = 10.
# The 2nd largest level sum is 13.

# Example 2:

#     1
#         2
#             3

# Input: root = [1,2,null,3], k = 1
# Output: 3
# Explanation: The largest level sum is 3.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def kthLargestLevelSum(root, k):
    sums = []

    def f_next(tree, i=0):
        if not tree:
            return
        nonlocal sums
        if len(sums) <= i:
            sums.append(tree.val)
        else: 
            sums[i] += tree.val
        f_next(tree.left, i+1)
        f_next(tree.right, i+1)
    
    f_next(root)
    sums = sorted(sums, reverse=True)
    return sums[k-1] if k <= len(sums) else -1

if __name__ == '__main__':
    print(kthLargestLevelSum([5,8,9,2,1,3,7,4,6], k = 2))  # 13
    print(kthLargestLevelSum([1,2,None,3], k = 1))  # 3
