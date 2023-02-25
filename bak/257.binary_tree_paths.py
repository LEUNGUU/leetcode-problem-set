# Binary Tree Paths
#
# [Easy] [AC:51.3% 322K of 628K] [filetype:python3]
#
# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input:
#
#    1
#
#  /   \
#
# 2     3
#
#  \
#
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def buildpath(root, path):
            if root:
                path = f"{path}{root.val}"
                if not root.left and not root.right:  # If reach a leaf
                    paths.append(path)  # update paths
                else:
                    path = f"{path}->"  # extend the current path
                    buildpath(root.left, path)
                    buildpath(root.right, path)

        paths = []
        buildpath(root, "")
        return paths


# iterative
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, f"{path}->{node.left.val}"))
            if node.right:
                stack.append((node.right, f"{path}->{node.right.val}"))
        return paths
