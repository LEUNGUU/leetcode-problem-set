# Majority Element
#
# [Easy] [AC:58.3% 645.3K of 1.1M] [filetype:python3]
#
# Given an array of size n, find the majority element. The majority
# element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element
# always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
#
# Output: 3
#
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
#
# Output: 2
#
# [End of Description]:

# brute force(Not Accepted, Timeout)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         majority = len(nums) // 2
#         for item in nums:
#             count = sum(1 for num in nums if num == item)
#             if count > majority:
#                 return item

# HashMap
# from collections import Counter
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = Counter(nums)
#         return max(count.keys(), key=count.get)

# sorting(since majority is more than n/2, it is save to pick the middle one after sorting)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums) // 2]

# randomization
import random


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for item in nums if item == candidate) > majority:
                return candidate
