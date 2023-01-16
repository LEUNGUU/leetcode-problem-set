from typing import Optional, Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(
            node: TreeNode, left: Union[float, int], right: Union[float, int]
        ) -> bool:
            if not node:
                return True
            if not (left < node.val < right):
                return False

            left_subtree = validate(node.left, left, node.val)
            right_subtree = validate(node.right, node.val, right)
            return left_subtree and right_subtree

        return validate(root, float("-inf"), float("inf"))
