# Reverse Integer
#
# [Easy] [AC:25.7% 1.1M of 4.1M] [filetype:python3]
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
#
# Output: 321
#
# Example 2:
#
# Input: -123
#
# Output: -321
#
# Example 3:
#
# Input: 120
#
# Output: 21
#
# Note:
#
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.
#
# [End of Description]:
# Pop and Push Digits & Check before Overflow
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        negative, x = (1, -x) if x < 0 else (0, x)
        while x >= 1:
            digit = x % 10
            x = x // 10
            result = result * 10 + digit
        if result > 2 ** 31 - 1 or -(result) <= -(2 ** 31):
            return 0
        return -(result) if negative else result
