# Partition Equal Subset Sum
#
# [Medium] [AC:44.0% 205.3K of 466.4K] [filetype:python3]
#
# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such
# that the sum of elements in both subsets is equal.
#
# Note:
#
# Each of the array element will not exceed 100.
#
# The array size will not exceed 200.
#
# Example 1:
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
# Example 2:
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.
#
# [End of Description]:
# bag
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total = sum(nums)
#         # sum cannot be divided by 2
#         if total % 2 != 0:
#             return False
#         capacity = sum(nums) // 2
#         sz = len(nums)
#         # initialize dp
#         dp = []
#         for _ in range(sz+1):
#             inner1 = []
#             for _ in range(capacity+1):
#                 inner1.append(False)
#             dp.append(inner1)
#
#         # base case
#         for i in range(sz+1):
#             dp[i][0] = True
#
#         # since we use i - 1 to call nums, so we need to add one to the size
#         # i must start from 1
#         for i in range(1, sz+1):
#             # need to include capacity itself
#             # j must start from 1, since 0 is the base case
#             for j in range(1, capacity+1):
#                 # judge if there is enough space for i
#                 if j - nums[i - 1] >= 0:
#                     # dp[i][j] = dp[i - 1][j]
#                 # else:
#                     dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
#         return dp[sz][capacity]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        capacity = sum(nums) // 2
        sz = len(nums)
        dp = [False] * (capacity + 1)
        # base case
        dp[0] = True

        for i in range(sz):
            for j in range(capacity, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]
        return dp[capacity]
