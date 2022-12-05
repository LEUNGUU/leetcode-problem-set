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
# recursive
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        # switch two children
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root


# iterative
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        node_list = [root]
        while node_list:
            node = node_list.pop()
            node.left, node.right = node.right, node.left
            if node.left is not None:
                node_list.append(node.left)
            if node.right is not None:
                node_list.append(node.right)
        return root
