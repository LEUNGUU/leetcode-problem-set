# Palindrome Linked List
#
# [Easy] [AC:39.0% 421.5K of 1.1M] [filetype:python3]
#
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
#
# Output: false
#
# Example 2:
#
# Input: 1->2->2->1
#
# Output: true
#
# Follow up:
#
# Could you do it in O(n) time and O(1) space?
#
# [End of Description]:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Copy to array and compare with array
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         vals = []
#         cur = head
#         while cur is not None:
#             vals.append(cur.val)
#             cur = cur.next
#         return vals == vals[::-1]

# recursive, worst than the first one, since this method limits the maximum element of linked list
# that can be handled due to the maximum stack frame of Python(which is 1000)
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         self.first_pointer = head

#         def recursiveCheck(current_node=head):
#             if current_node is not None:
#                 if not recursiveCheck(current_node.next):
#                     return False
#                 if self.first_pointer.val != current_node.val:
#                     return False
#                 self.first_pointer = self.first_pointer.next
#             return True
#         return recursiveCheck()


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # find the end of first half and reverse second half
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # check if there is a Palindrome
        result = True
        first_pointer = head
        second_pointer = second_half_start
        while result and second_pointer is not None:
            if first_pointer.val != second_pointer.val:
                result = False
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

        # resore the list and return result
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, node: ListNode) -> ListNode:
        fast = node
        slow = node
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, node: ListNode) -> ListNode:
        previous = None
        current = node
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
