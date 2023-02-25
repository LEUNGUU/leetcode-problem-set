# Remove Linked List Elements
#
# [Easy] [AC:37.6% 326.1K of 866.4K] [filetype:python3]
#
# Remove all elements from a linked list of integers that have value
# val.
#
# Example:
#
# Input:  1->2->6->3->4->5->6, val = 6
#
# Output: 1->2->3->4->5
#
# [End of Description]:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# add a sentinel node(sentinel stand still, pre and cur go through the list)
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        pre, cur = sentinel, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return sentinel.next
