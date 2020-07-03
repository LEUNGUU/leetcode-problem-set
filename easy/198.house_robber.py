# House Robber
# 
# [Easy] [AC:41.9% 514.9K of 1.2M] [filetype:python3]
# 
# You are a professional robber planning to rob houses along
# a street. Each house has a certain amount of money stashed, the
# only constraint stopping you from robbing each of them is that
# adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken
# into on the same night.
# 
# Given a list of non-negative integers representing the amount of
# money of each house, determine the maximum amount of money you can
# rob tonight without alerting the police.
# 
# Example 1:
# 
# Input: nums = [1,2,3,1]
# 
# Output: 4
# 
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money
# = 3).
# 
#              Total amount you can rob = 1 + 3 = 4.
# 
# Example 2:
# 
# Input: nums = [2,7,9,3,1]
# 
# Output: 12
# 
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and
# rob house 5 (money = 1).
# 
#              Total amount you can rob = 2 + 9 + 1 = 12.
# 
# Constraints:
# 
# 0 <= nums.length <= 100
# 
# 0 <= nums[i] <= 400
# 
# [End of Description]:
# DP method, consider the simplest cases first, then drive a more complicated one.
class Solution:
    def rob(self, nums: List[int]) -> int:
        first_sum, second_sum = 0, 0
        for item in nums:
            cur_sum = max(first_sum + item, second_sum)
            first_sum = second_sum
            second_sum = cur_sum
        return second_sum

