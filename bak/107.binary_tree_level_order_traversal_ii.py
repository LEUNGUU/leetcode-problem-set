# Binary Tree Level Order Traversal II
#
# [Easy] [AC:51.3% 304.5K of 593.1K] [filetype:python3]
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
#
# For example:
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
# return its bottom-up level order traversal as:
#
# [
#
#   [15,7],
#
#   [9,20],
#
#   [3]
#
# ]
#
# [End of Description]:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# RecursionL DFS
from typing import Dict


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        dfs_result = {}
        dfs_result = self.traverse(root, 1, dfs_result)

        result = []
        for key in reversed(dfs_result.keys()):
            result.append(dfs_result[key])
        return result

    # DFS
    def traverse(
        self, node: TreeNode, level: int, dictionary: Dict[int, List[int]]
    ) -> Dict[int, List[int]]:
        if node:
            if level not in dictionary:
                dictionary.update({level: []})
            dictionary[level].append(node.val)
            self.traverse(node.left, level + 1, dictionary)
            self.traverse(node.right, level + 1, dictionary)
        return dictionary


# Iteration: BFS
from collections import deque


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        q = deque()
        result = []
        if root is None:
            return result
        q.append(root)
        while q:
            level_size = len(q)
            values = []
            # go over all the node in the same level
            for _ in range(level_size):
                # Make sure the order is from left to right
                item = q.popleft()
                values.append(item.val)
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            result.append(values)
        return reversed(result)
