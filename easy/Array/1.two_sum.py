# Two Sum
#
# [Easy] [AC:45.4% 2.9M of 6.4M] [filetype:python3]
#
# Given an array of integers, return indices of the
# two numbers such that they add up to a specific
# target.
#
# You may assume that each input would have exactly
# one solution, and you may not use the same
# element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
#
# return [0, 1].
#
# [End of Description]:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for index, value in enumerate(nums):
            res = target - value
            if res in result:
                return [index, result[res]]
            else:
                result[value] = index
