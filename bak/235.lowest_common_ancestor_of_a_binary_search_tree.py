# Lowest Common Ancestor of a Binary Search Tree
#
# [Easy] [AC:49.5% 400.8K of 810.2K] [filetype:python3]
#
# Given a binary search tree (BST), find the lowest common ancestor
# (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common
# ancestor is defined between two nodes p and q as the lowest node in
# T that has both p and q as descendants (where we allow a node to be
# a descendant of itself).”
#
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
#
# Example 1:
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#
# Output: 6
#
# Explanation: The LCA of nodes 2 and 8 is 6.
#
# Example 2:
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
#
# Output: 2
#
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be
# a descendant of itself according to the LCA definition.
#
# Constraints:
#
# All of the nodes' values will be unique.
#
# p and q are different and both values will exist in the BST.
#
# [End of Description]:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Recursive
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Value of current node or parent node
        root_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # Both nodes are at the right of root(greater than parent)
        if p_val > root_val and q_val > root_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # Both nodes are at the left of root(lesser than parent)
        elif p_val < root_val and q_val < root_val:
            return self.lowestCommonAncestor(root.left, p, q)
        # we have found the split point
        else:
            # Found it
            return root


# Iterative
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Value of p
        p_val = p.val
        # Value of q
        q_val = q.val

        # Start from the root node of the tree
        node = root

        # traverse the tree
        while node:
            # Value of current node or parent
            root_val = node.val

            if p_val > root_val and q_val > root_val:
                # If both p and q are greater than parent
                node = node.right
            elif p_val < root_val and q_val < root_val:
                # If bot p and q are lesser than parent
                node = node.left
            else:
                # Found it
                return node
