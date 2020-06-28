# Linked List Cycle
#
# [Easy] [AC:40.7% 628.9K of 1.5M] [filetype:python3]
#
# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which
# represents the position (0-indexed) in the linked list where tail connects
# to. If pos is -1, then there is no cycle in the linked list.
#
# Example 1:
#
# Input: head = [3,2,0,-4], pos = 1
#
# Output: true
#
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
#
# Example 2:
#
# Input: head = [1,2], pos = 0
#
# Output: true
#
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
#
# Example 3:
#
# Input: head = [1], pos = -1
#
# Output: false
#
# Explanation: There is no cycle in the linked list.
#
# Follow up:
#
# Can you solve it using O(1) (i.e. constant) memory?
#
# [End of Description]:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# list to record nodes' references
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         vals = []
#         while head is not None:
#             if head not in vals:
#                 vals.append(head)
#             else:
#                 return True
#             head = head.next
#         return False

# two pointers, one is slow pointer and the other is fast pointer
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slow_pointer = head
        fast_pointer = head.next
        while slow_pointer != fast_pointer:
            if fast_pointer is None or fast_pointer.next is None:
                return False
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return True
