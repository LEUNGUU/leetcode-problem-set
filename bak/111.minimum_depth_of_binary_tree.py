# Minimum Depth of Binary Tree
#
# [Easy] [AC:37.2% 408.5K of 1.1M] [filetype:python3]
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path
# from the root node down to the nearest leaf node.
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
# return its minimum depth = 2.
#
# [End of Description]:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS strategy (recursion)
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        # we are at leaf node
        children = [root.left, root.right]
        if not any(children):
            return 1

        min_depth = float("inf")
        # check every child
        # min depth is always minimum
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return 1 + min_depth


# DFS strategy (iteration)
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            stack, min_depth = [(1, root)], float("inf")
        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    stack.append((depth + 1, c))
        return min_depth


# BFS strategy
from collections import deque


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            node_deque = deque([(1, root)])

        while node_deque:
            depth, root = node_deque.popleft()
            children = [root.left, root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth + 1, c))
