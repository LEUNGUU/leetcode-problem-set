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

# Recursion
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# Iteration
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # maintain an unchaing reference to node ahead of the return node
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next


# self-defined solution
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
