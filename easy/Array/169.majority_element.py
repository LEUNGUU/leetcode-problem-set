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
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        for item in nums:
            count = sum(1 for num in nums if num == item)
            if count > majority:
                return item


# HashMap
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max(count.keys(), key=count.get)


# sorting(since majority is more than n/2, it is save to pick the middle one after sorting)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


# randomization
import random


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for item in nums if item == candidate) > majority:
                return candidate


#  Divide and Conquer
class Solution:
    def majorityElement(self, nums: List[int], lo=0, hi=None) -> int:
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            # if the two halves agree on the majority element,
            # return it
            if left == right:
                return left

            # otherwise, count each element and return the winner
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)


# Boyer-Moore Voting Algorithm
# [7, 7, 5, 7, 5, 1|5, 7|5, 5, 7, 7|7, 7, 7, 7], we use pipe when count equals 0
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
