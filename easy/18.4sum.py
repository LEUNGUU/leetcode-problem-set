# 4Sum
#
# [Medium] [AC:33.9% 352.6K of 1M] [filetype:python3]
#
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that
# a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
#
# [
#
#   [-1,  0, 0, 1],
#
#   [-2, -1, 1, 2],
#
#   [-2,  0, 0, 2]
#
# ]
#
# [End of Description]:
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(nums)
        return self.nSumTarget(sorted_nums, 4, 0, target)

    def nSumTarget(self, nums: List[int], n: int, start: int, target: int) -> List[List[int]]:
        sz = len(nums)
        res = []
        if n < 2 or sz < n:
            return res
        if n == 2:
            lo = start
            hi = sz - 1
            while lo < hi:
                total = nums[lo] + nums[hi]
                left = nums[lo]
                right = nums[hi]
                if total > target:
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                elif total < target:
                    while lo < hi and nums[lo] == left:
                        lo += 1
                elif total == target:
                    res.append([left, right])
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    while lo < hi and nums[hi] == right:
                        hi -= 1
        else:
            i = start
            while i < sz:
                sub = self.nSumTarget(nums, n - 1, i + 1, target - nums[i])
                for item in sub:
                    item.append(nums[i])
                    res.append(item)
                while (i < sz - 1) and (nums[i] == nums[i + 1]):
                    i += 1
                i += 1
        return [sorted(item) for item in res]






