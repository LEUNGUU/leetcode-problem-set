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
            elif nums[pa] == 0 and nums[pb] == 0:
                pass
            else:
                pa += 1
            pb += 1
