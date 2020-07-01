# Excel Sheet Column Number
#
# [Easy] [AC:54.2% 286.3K of 528.3K] [filetype:python3]
#
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
#
# For example:
#
#     A -> 1
#
#     B -> 2
#
#     C -> 3
#
#     ...
#
#     Z -> 26
#
#     AA -> 27
#
#     AB -> 28
#
#     ...
#
# Example 1:
#
# Input: "A"
#
# Output: 1
#
# Example 2:
#
# Input: "AB"
#
# Output: 28
#
# Example 3:
#
# Input: "ZY"
#
# Output: 701
#
# Constraints:
#
# 1 <= s.length <= 7
#
# s consists only of uppercase English letters.
#
# s is between "A" and "FXSHRXW".
#
# [End of Description]:
class Solution:
    def titleToNumber(self, s: str) -> int:
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        rs = reversed(s)
        times = 0
        res = 0
        for item in rs:
            res += (int(abc.index(item)) + 1) * int(math.pow(26, times))
            times += 1
        return res
