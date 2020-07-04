# Invert Binary Tree
#
# [Easy] [AC:64.5% 532K of 824.8K] [filetype:python3]
#
# Invert a binary tree.
#
# Example:
#
# Input:
#
#      4
#
#    /   \
#
#   2     7
#
#  / \   / \
#
# 1   3 6   9
#
# Output:
#
#      4
#
#    /   \
#
#   7     2
#
#  / \   / \
#
# 9   6 3   1
#
# Trivia:
#
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew),
# but you can’t invert a binary tree on a whiteboard so f*** off.
#
# [End of Description]:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        # switch two children
        self.invertTree(root.left)
        self.invertTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root
