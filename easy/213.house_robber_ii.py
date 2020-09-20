# House Robber II
#
# [Medium] [AC:36.6% 187.6K of 512.6K] [filetype:python3]
#
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent
# houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
# money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [2,3,2]
#
# Output: 3
#
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#
#              because they are adjacent houses.
#
# Example 2:
#
# Input: [1,2,3,1]
#
# Output: 4
#
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#
#              Total amount you can rob = 1 + 3 = 4.
#
# [End of Description]:
class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(nums: List[int], start: int, end: int):
            dp_i_1 = dp_i_2 = dp_i = 0
            for item in nums[start:end]:
                dp_i = max(dp_i_1, dp_i_2 + item)
                dp_i_2 = dp_i_1
                dp_i_1 = dp_i
            return dp_i
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(robRange(nums, 0, n - 1), robRange(nums, 1, n))


