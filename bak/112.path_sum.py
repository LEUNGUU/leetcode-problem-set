# Path Sum
#
# [Easy] [AC:40.8% 465.3K of 1.1M] [filetype:python3]
#
# Given a binary tree and a sum, determine if the tree has
# a root-to-leaf path such that adding up all the values along the
# path equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#
#      / \
#
#     4   8
#
#    /   / \
#
#   11  13  4
#
#  /  \      \
#
# 7    2      1
#
# return true, as there exist a root-to-leaf path 5->4->11->2 which
# sum is 22.
#
# [End of Description]:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# DFS strategy
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        else:
            stack = [(root, root.val)]
            while stack:
                node, total = stack.pop()
                children = [node.left, node.right]
                # we are leaf
                if not any(children):
                    if total == sum:
                        return True
                for c in children:
                    if c:
                        stack.append((c, total + c.val))
            return False


# Another version of Iteration
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        de = [
            (root, sum - root.val),
        ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False


# Recursion
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
