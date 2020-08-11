# Closest Binary Search Tree Value
#
# [Easy] [AC:48.5% 147.7K of 304.4K] [filetype:python3]
#
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
#
# Note:
#
# Given target value is a floating point.
#
# You are guaranteed to have only one unique value in the BST that is closest to the target.
#
# Example:
#
# Input: root = [4,2,5,1,3], target = 3.714286
#
#     4
#
#    / \
#
#   2   5
#
#  / \
#
# 1   3
#
# Output: 4
#
# [End of Description]:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack = []
        minimum = float("inf")
        res = 0
        stack.append(root)
        while stack:
            node = stack.pop()
            if abs(node.val - target) < minimum:
                minimum = abs(node.val - target)
                res = node.val
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return res
