# Convert Sorted Array to Binary Search Tree
#
# [Easy] [AC:56.9% 393.2K of 690.5K] [filetype:python3]
#
# Given an array where elements are sorted in ascending order, convert it to
# a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
#
# Example:
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
#
#       0
#
#      / \
#
#    -3   9
#
#    /   /
#
#  -10  5
#
# [End of Description]:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        def bst_recursive(nums: List[int], start: int, end: int) -> TreeNode:
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = bst_recursive(nums, start, mid - 1)
            node.right = bst_recursive(nums, mid + 1, end)
            return node

        return bst_recursive(nums, 0, len(nums) - 1)
