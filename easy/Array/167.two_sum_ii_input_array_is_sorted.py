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

# two pointer
# since the array is sorted in ascending order, then we can use two pointer
# one from small to large, the other from large to small
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            cur_sum = numbers[i] + numbers[j]
            if cur_sum == target:
                return [i + 1, j + 1]
            elif cur_sum < target:
                i += 1
            else:
                j -= 1
        return []


# binary search(Actually it is like two pointer, one is left and the other is right)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = left + (right - left) // 2
            res = numbers[left] + numbers[right]
            if res == target:
                return [left + 1, right + 1]
            elif res < target:
                left = mid if numbers[mid] + numbers[right] < target else left + 1
            else:
                right = mid if numbers[mid] + numbers[left] > target else right - 1
        return []
