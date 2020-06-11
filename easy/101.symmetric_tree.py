# Symmetric Tree
# 
# [Easy] [AC:46.4% 629.1K of 1.4M] [filetype:python3]
# 
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
#     1
# 
#    / \
# 
#   2   2
# 
#  / \ / \
# 
# 3  4 4  3
# 
# But the following [1,2,2,null,3,null,3] is not:
# 
#     1
# 
#    / \
# 
#   2   2
# 
#    \   \
# 
#    3    3
# 
# Follow up: Solve it both recursively and iteratively.
# 
# [End of Description]:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (t1.val == t2.val) and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)


