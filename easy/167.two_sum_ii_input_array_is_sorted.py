# Two Sum II - Input array is sorted
#
# [Easy] [AC:53.7% 404.8K of 754.5K] [filetype:python3]
#
# Given an array of integers that is already sorted in ascending order, find
# two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they
# add up to the target, where index1 must be less than index2.
#
# Note:
#
# Your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.
#
# Example:
#
# Input: numbers = [2,7,11,15], target = 9
#
# Output: [1,2]
#
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
#
# [End of Description]:
# hash table
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         res = {}
#         for index, value in enumerate(numbers):
#             rest = target - value
#             if rest in res:
#                 return [res[rest], index + 1]
#             else:
#                 res[value] = index + 1
# two pointer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

