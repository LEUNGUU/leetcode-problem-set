# House Robber III
#
# [Medium] [AC:50.8% 168.4K of 331.4K] [filetype:python3]
#
# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the
# "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that
# "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses
# were broken into on the same night.
#
# Determine the maximum amount of money the thief can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [3,2,3,null,3,null,1]
#
#      3
#
#     / \
#
#    2   3
#
#     \   \
#
#      3   1
#
# Output: 7
#
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
#
# Example 2:
#
# Input: [3,4,5,1,3,null,1]
#
#      3
#
#     / \
#
#    4   5
#
#   / \   \
#
#  1   3   1
#
# Output: 9
#
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
#
# [End of Description]:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time exceeds
# class Solution:
#     def rob(self, root: TreeNode) -> int:
#         memo = {}
#         if root is None:
#             return 0
#         if root in memo:
#             return memo[root]
#         # rob, then go to next after next
#         left = (self.rob(root.left.left) + self.rob(root.left.right)) if root.left is not None else 0
#         right = (self.rob(root.right.left) + self.rob(root.right.right)) if root.right is not None else 0
#         do_it = root.val + left + right
#         # not rob, go to next
#         not_do = self.rob(root.right) + self.rob(root.left)
#
#         # write into memo
#         memo[root] = max(do_it, not_do)
#         return memo[root]


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dp(root: TreeNode):
            if root is None:
                return [0, 0]
            do_it = root.val + dp(root.left)[0] + dp(root.right)[0]
            not_do = max(dp(root.left)[0], dp(root.left)[1]) + max(
                dp(root.right)[0], dp(root.right)[1]
            )
            return [not_do, do_it]

        return max(dp(root)[0], dp(root)[1])
