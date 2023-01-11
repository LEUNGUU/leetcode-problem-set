from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True

        if self.sameTree(root, subRoot):
            return True
        left_res: bool = self.isSubtree(root.left, subRoot)
        right_res: bool = self.isSubtree(root.right, subRoot)
        return left_res or right_res

    def sameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            left_res: bool = self.sameTree(s.left, t.left)
            right_res: bool = self.sameTree(s.right, t.right)
            return left_res and right_res
        return False
