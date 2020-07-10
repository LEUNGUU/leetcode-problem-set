# Strobogrammatic Number
#
# [Easy] [AC:44.8% 78.6K of 175.3K] [filetype:python3]
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
#
# Write a function to determine if a number is strobogrammatic. The number is
# represented as a string.
#
# Example 1:
#
# Input: num = "69"
#
# Output: true
#
# Example 2:
#
# Input: num = "88"
#
# Output: true
#
# Example 3:
#
# Input: num = "962"
#
# Output: false
#
# Example 4:
#
# Input: num = "1"
#
# Output: true
#
# [End of Description]:
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobos = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        left, right = 0, len(num) - 1
        while left <= right:
            left_num, right_num = num[left], num[right]
            if (
                left_num not in strobos
                or right_num not in strobos
                or strobos[left_num] != right_num
            ):
                return False
            left += 1
            right -= 1
        return True
