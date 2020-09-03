# Add Digits
#
# [Easy] [AC:57.6% 316.2K of 548.9K] [filetype:python3]
#
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# Example:
#
# Input: 38
#
# Output: 2
#
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
#
#              Since 2 has only one digit, return it.
#
# Follow up:
#
# Could you do it without any loop/recursion in O(1) runtime?
#
# [End of Description]:
# class Solution:
#     def addDigits(self, num: int) -> int:
#         if len(str(num)) == 1:
#             return num
#         while len(str(num)) > 1:
#             digits = []
#             while num > 0:
#                 num, digit = divmod(num, 10)
#                 digits.append(digit)
#             num = sum(digits)
#         return num

# n mod 9 = (d0 + d1 + ... + dn) mode 9
class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
