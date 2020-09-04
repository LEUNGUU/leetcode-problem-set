# Balanced Binary Tree
#
# [Easy] [AC:43.2% 442.1K of 1M] [filetype:python3]
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#     3
#
#    / \
#
#   9  20
#
#     /  \
#
#    15   7
#
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#        1
#
#       / \
#
#      2   2
#
#     / \
#
#    3   3
#
#   / \
#
#  4   4
#
# Return false.
#
# [End of Description]:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# top down solution
# class Solution:
#     def height(self, node: TreeNode) -> int:
#         if not node:
#             return -1
#         # recursive calculate the height
#         return 1 + max(self.height(node.left), self.height(node.right))
#
#
#     def isBalanced(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         # every subtree must be balanced
#         return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

# bottom up solution
class Solution:
    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        if not root:
            return True, -1

        # perform left
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0

        # perform right
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0

        # after checking subtrees, check current one
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]
