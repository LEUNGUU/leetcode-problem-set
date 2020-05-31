# Merge Two Sorted Lists
# 
# [Easy] [AC:52.6% 962.7K of 1.8M]
# [filetype:python3]
# 
# Merge two sorted linked lists and return it
# as a new sorted list. The new list should be
# made by splicing together the nodes of the
# first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# 
# Output: 1->1->2->3->4->4
# 
# [End of Description]:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        pointer = head
        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                pointer.next = l2
                break
            elif l2 is None:
                pointer.next = l1
                break
            else:
                small = 0
                if l1.val > l2.val:
                    small = l2.val
                    l2 = l2.next
                else:
                    small = l1.val
                    l1 = l1.next
                new = ListNode(small)
                pointer.next = new
                pointer = pointer.next
        return head.next



