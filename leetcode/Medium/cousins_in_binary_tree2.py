# https://leetcode.com/problems/cousins-in-binary-tree-ii/description/

# Given the root of a binary tree, replace the value of each node in the tree 
# with the sum of all its cousins' values.
# Two nodes of a binary tree are cousins if they have the same depth with different parents.
# Return the root of the modified tree.
# Note that the depth of a node is the number of edges in the path from the root node to it.

# Example 1:

#             5                          0
#         4       9     -->           0       0
#     1   10       7               7    7       11   

# Input: root = [5,4,9,1,10,null,7]
# Output: [0,0,0,7,7,null,11]
# Explanation: The diagram above shows the initial binary tree and the 
# binary tree after changing the value of each node.
# - Node with value 5 does not have any cousins so its sum is 0.
# - Node with value 4 does not have any cousins so its sum is 0.
# - Node with value 9 does not have any cousins so its sum is 0.
# - Node with value 1 has a cousin with value 7 so its sum is 7.
# - Node with value 10 has a cousin with value 7 so its sum is 7.
# - Node with value 7 has cousins with values 1 and 10 so its sum is 11.

# Example 2:

#             3                          0
#         1       2     -->          0       0

# Input: root = [3,1,2]
# Output: [0,0,0]
# Explanation: The diagram above shows the initial binary tree and the binary tree 
# after changing the value of each node.
# - Node with value 3 does not have any cousins so its sum is 0.
# - Node with value 1 does not have any cousins so its sum is 0.
# - Node with value 2 does not have any cousins so its sum is 0.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def replaceValueInTree(root):
    sums = [0]

    def count_sums(tree, i=0):
        if not tree:
            return
        nonlocal sums
        if i >= len(sums):
            sums.append(tree.val)
        else:
            sums[i] += tree.val
        count_sums(tree.left, i+1)
        count_sums(tree.right, i+1)
    
    count_sums(root)
    root.val = 0
    tree2 = TreeNode(val = 0)

    def count_cousins(tree, tree2, i=0):
        if not tree:
            return
        nonlocal sums
        if tree.left:
            tree2.left = TreeNode(sums[i+1] - tree.left.val)
            if tree.right:
                tree2.left.val -= tree.right.val
        if tree.right:
            tree2.right = TreeNode(sums[i+1] - tree.right.val)
            if tree.left:
                tree2.right.val -= tree.left.val
        count_cousins(tree.left, tree2.left, i+1)
        count_cousins(tree.right, tree2.right, i+1)
    
    count_cousins(root, tree2)
    return tree2
