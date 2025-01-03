# https://leetcode.com/problems/add-two-numbers/description/

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(l1, l2):
        l3 = ListNode((l1.val + l2.val) % 10)
        add = (l1.val + l2.val) // 10
        while l1.next or l2.next:
            node = add
            if l1.next:
                node += l1.next.val
                l1 = l1.next
            if l2.next:
                node += l2.next.val
                l2 = l2.next
            add = node // 10
            node = node % 10
            n = l3
            while n.next:
                n = n.next
            n.next = ListNode(node)
        if add == 1:
            n = l3
            while n.next:
                n = n.next
            n.next = ListNode(1)
        return l3
