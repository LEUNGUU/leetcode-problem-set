from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal res
            res = max(res, 2 + left + right)

            return 1 + max(left, right)
        dfs(root)
        return res
