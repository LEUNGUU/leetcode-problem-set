# Range Sum Query - Immutable
#
# [Easy] [AC:44.9% 209.2K of 466.1K] [filetype:python3]
#
# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Example:
#
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
#
# sumRange(2, 5) -> -1
#
# sumRange(0, 5) -> -3
#
# Constraints:
#
# You may assume that the array does not change.
#
# There are many calls to sumRange function.
#
# 0 <= nums.length <= 10^4
#
# -10^5 <= nums[i] <= 10^5
#
# 0 <= i <= j < nums.length
#
# [End of Description]:

# Not a formal solution, my own one
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        # return sum([self.nums[idx] for idx in range(i, j+1)])
        return sum(self.nums[i : j + 1])


# Caching
class NumArray:
    def __init__(self, nums: List[int]):
        self.res = [0] * (len(nums) + 1)
        for idx in range(len(nums)):
            self.res[idx + 1] = self.res[idx] + nums[idx]

    def sumRange(self, i: int, j: int) -> int:
        return self.res[j + 1] - self.res[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
