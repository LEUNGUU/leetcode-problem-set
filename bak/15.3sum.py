# 3Sum
#
# [Medium] [AC:27.1% 1M of 3.8M] [filetype:python3]
#
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique
# triplets in the array which gives the sum of zero.
#
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
#
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
#
# Input: nums = []
#
# Output: []
#
# Example 3:
#
# Input: nums = [0]
#
# Output: []
#
# Constraints:
#
# 0 <= nums.length <= 3000
#
# -105 <= nums[i] <= 105
#
# [End of Description]:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        return self.nSumTarget(sorted_nums, 3, 0, 0)

    def nSumTarget(
        self, nums: List[int], n: int, start: int, target: int
    ) -> List[List[int]]:
        sz = len(nums)
        res: List[List[int]] = []
        if n < 2 or sz < n:
            return res
        if n == 2:
            lo = start
            hi = sz - 1
            while lo < hi:
                total = nums[lo] + nums[hi]
                left = nums[lo]
                right = nums[hi]
                if total == target:
                    res.append([left, right])
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                elif total < target:
                    while lo < hi and nums[lo] == left:
                        lo += 1
                elif total > target:
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
