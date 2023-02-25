# Missing Number
#
# [Easy] [AC:51.7% 474.5K of 917.4K] [filetype:python3]
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
#
# Output: 2
#
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
#
# Output: 8
#
# Note:
#
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space
# complexity?
#
# [End of Description]:


# Sorting
# It is easy to find which number is missing.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        # Ensure n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure 0 is at the first index
        if nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range(0, n)
        for i in range(1, len(nums)):
            # here we loop from 1 (0 is here)
            # we use nums[i - 1] to leverage nums[0]
            expected_number = nums[i - 1] + 1
            if nums[i] != expected_number:
                return expected_number


# HashSet
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        # since we miss one element, the we plus one
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number


# Gauss's Formula
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n * (n + 1) // 2) - sum(nums)


# Bit Manipulation
# XOR, same will return 0 and different will return 1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lost = len(nums)
        for index, num in enumerate(nums):
            lost ^= index ^ num
        return lost
