# Move Zeroes
#
# [Easy] [AC:57.8% 877K of 1.5M] [filetype:python3]
#
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
# non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
#
# Output: [1,3,12,0,0]
#
# Note:
#
# You must do this in-place without making a copy of the array.
#
# Minimize the total number of operations.
#
# [End of Description]:
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         while n > 0:
#             if nums[-n] == 0:
#                 nums.remove(nums[-n])
#                 nums.append(0)
#             n -= 1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pa, pb = 0, 1
        while pb < len(nums):
            if nums[pa] == 0 and nums[pb] != 0:
                nums[pa], nums[pb] = nums[pb], nums[pa]
                pa += 1
                pb += 1
            elif nums[pa] == 0 and nums[pb] == 0:
                pb += 1
            else:
                pa += 1
                pb += 1
