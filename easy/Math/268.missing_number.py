# Missing Number
#
# [Easy] [AC:51.7% 474.5K of 917.4K] [filetype:python3]
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
#
# Output: 2
#
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
#
# Output: 8
#
# Note:
#
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space
# complexity?
#
# [End of Description]:
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         return (n * (n + 1) // 2) - sum(nums)

# XOR, same will return 0 and different will return 1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lost = len(nums)
        for index, num in enumerate(nums):
            lost ^= index ^ num
        return lost
