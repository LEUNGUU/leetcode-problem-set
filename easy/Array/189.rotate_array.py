# Rotate Array
#
# [Easy] [AC:34.3% 486.4K of 1.4M] [filetype:python3]
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
#
# Follow up:
#
# Try to come up as many solutions as you can, there are at least
# 3 different ways to solve this problem.
#
# Could you do it in-place with O(1) extra space?
#
# Example 1:
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
#
# Output: [5,6,7,1,2,3,4]
#
# Explanation:
#
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
#
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
#
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# Example 2:
#
# Input: nums = [-1,-100,3,99], k = 2
#
# Output: [3,99,-1,-100]
#
# Explanation:
#
# rotate 1 steps to the right: [99,-1,-100,3]
#
# rotate 2 steps to the right: [3,99,-1,-100]
#
# Constraints:
#
# 1 <= nums.length <= 2 * 10^4
#
# It's guaranteed that nums[i] fits in a 32 bit-signed integer.
#
# k >= 0
#
# [End of Description]:

# brute force(Not Accepted, Time Limit Exceeded)
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         # speed up the rotation
#         k %= len(nums)
#
#         for i in range(k):
#             previous = nums[-1]
#             for j in range(len(nums)):
#                 nums[j], previous = previous, nums[j]

# Using Extra Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
        nums[:] = a


# Using Cyclic Replacement
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        start, count = 0, 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n


# list manuplication
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for _ in range(k):
#             nums.insert(0, nums.pop())

# class Solution:
#     def reverse(self, nums: List[int], start: int, end: int) -> List[int]:
#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start, end = start + 1, end - 1

#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         # k is not numbers of nums, it is numbers of steps
#         k %= n
#         self.reverse(nums, 0, n - 1)
#         self.reverse(nums, 0, k - 1)
#         self.reverse(nums, k, n - 1)


# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         # k means steps, not elements need to be rotate
#         k %= len(nums)
#         nums[0:] = nums[-k:] + nums[:-k]
