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
# one-pass hash table [Accepted]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for index, value in enumerate(nums):
            res = target - value
            if res in result:
                return [result[res], index]
            else:
                result[value] = index


#
#
# # two-pass hash table [Accepted]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # generate a dict which key is element, value is index
        nums_dict = {value: index for index, value in enumerate(nums)}
        # loop over to find results
        for index in range(len(nums)):
            res = target - nums[index]
            if res in nums_dict and nums_dict[res] != index:
                return [index, nums_dict[res]]


#
#
# # Bruce Force [Not Accepted, Time exceeded]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1 in range(len(nums)):
            for idx2 in range(idx1 + 1, len(nums)):
                if nums[idx1] + nums[idx2] == target:
                    return [idx1, idx2]


# two pointers
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            total = sorted_nums[lo] + sorted_nums[hi]
            left = sorted_nums[lo]
            right = sorted_nums[hi]
            if total > target:
                while lo < hi and sorted_nums[hi] == right:
                    hi -= 1
            elif total < target:
                while lo < hi and sorted_nums[lo] == left:
                    lo += 1
            elif total == target:
                res = []
                for index, item in enumerate(nums):
                    if item in [left, right]:
                        res.append(index)
                return res
        return []
