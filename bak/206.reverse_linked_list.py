# Reverse Linked List
#
# [Easy] [AC:61.9% 986.5K of 1.6M] [filetype:python3]
#
# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
#
# Output: 5->4->3->2->1->NULL
#
# Follow up:
#
# A linked list can be reversed either iteratively or recursively.
# Could you implement both?
#
# [End of Description]:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# iteratively
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


# recursively
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        # here we use invoke stack to keep the previous node
        pointer = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return pointer
