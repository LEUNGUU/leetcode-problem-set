# Excel Sheet Column Title
#
# [Easy] [AC:30.8% 216.3K of 702.4K] [filetype:python3]
#
# Given a positive integer, return its corresponding column title as
# appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#
#     2 -> B
#
#     3 -> C
#
#     ...
#
#     26 -> Z
#
#     27 -> AA
#
#     28 -> AB
#
#     ...
#
# Example 1:
#
# Input: 1
#
# Output: "A"
#
# Example 2:
#
# Input: 28
#
# Output: "AB"
#
# Example 3:
#
# Input: 701
#
# Output: "ZY"
#
# [End of Description]:
class Solution:
    def convertToTitle(self, n: int) -> str:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""
        while n:
            # alpha is starting from 0, but actually what we are doing is non-zero calculation
            n -= 1
            res = alpha[n % 26] + res
            n //= 26
        return res
