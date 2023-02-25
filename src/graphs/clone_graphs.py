from typing import Union

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> Union["Node", None]:
        oldToNew = {}

        def clone(node: "Node") -> "Node":
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy

        return clone(node) if node else None
