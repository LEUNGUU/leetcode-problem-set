from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        nodeMapping = {None: None}

        curr = head
        while curr:
            newNode = Node(curr.val)
            nodeMapping[curr] = newNode
            curr = curr.next

        curr = head
        while curr:
            newNode = nodeMapping[curr]
            newNode.next = nodeMapping[curr.next]
            newNode.random = nodeMapping[curr.random]
            curr = curr.next

        return nodeMapping[head]
