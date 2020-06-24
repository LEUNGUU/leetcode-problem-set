# Maximum Depth of Binary Tree
#
# [Easy] [AC:65.3% 796.5K of 1.2M] [filetype:python3]
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
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
# return its depth = 3.
#
# [End of Description]:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
