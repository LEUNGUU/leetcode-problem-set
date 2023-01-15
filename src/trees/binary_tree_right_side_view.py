from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res: List[int] = []
        q = deque([root])

        while q:
            rightSize = None
            queue_length = len(q)

            for _ in range(queue_length):
                node = q.popleft()
                if node:
                    rightSize = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSize:
                res.append(rightSize.val)
        return res
