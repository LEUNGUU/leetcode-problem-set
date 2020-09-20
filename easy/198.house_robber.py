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

# Let us look at the case n = 1, clearly f(1) = A1.
# Now, let us look at n = 2, which f(2) = max(A1, A2).
# For n = 3, you have basically the following two options:
# 1. Rob the third house, and add its amount to the first house's amount.
# 2. Do not rob the third house, and stick with the maximum amount of the first two houses.
# f(k) = max(f(k – 2) + Ak, f(k – 1))
# We choose base case asd f(-1) = f(0) = 0
#class Solution:
#    def rob(self, nums: List[int]) -> int:
#        first_sum, second_sum = 0, 0
#        for item in nums:
#            cur_sum = max(first_sum + item, second_sum)
#            first_sum = second_sum
#            second_sum = cur_sum
#        return second_sum

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#
#         def dp(nums: List[int], start: int, memo: List[int]):
#             if start >= len(nums):
#                 return 0
#             if memo[start] != -1:
#                 return memo[start]
#
#             memo[start] = max(dp(nums, start + 1, memo), nums[start] + dp(nums, start + 2, memo))
#             return memo[start]
#
#         # memory
#         memo = [-1] * len(nums)
#         return dp(nums, 0, memo)


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         dp= [-1] * len(nums)
#         for i in range(len(nums)-1, -1, -1):
#             dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
#         return dp[0]

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_i_1 = dp_i_2 = dp_i = 0
        for item in nums:
            dp_i = max(dp_i_1, dp_i_2 + item)
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i


