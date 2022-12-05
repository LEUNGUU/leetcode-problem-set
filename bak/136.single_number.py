# Single Number
#
# [Easy] [AC:65.2% 872K of 1.3M] [filetype:python3]
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
#
# Output: 1
#
# Example 2:
#
# Input: [4,1,2,1,2]
#
# Output: 4
#
# [End of Description]:

# list operation
# Iterate over all the elements in nums
# If some number in nums is new to array, append it
# If some number is already in the array, remove it
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = []
        for item in nums:
            if item in tmp:
                tmp.remove(item)
            else:
                tmp.append(item)
        return tmp.pop()


# hash table to record elements
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}
        for i in range(len(nums)):
            if nums[i] not in res:
                res[nums[i]] = 1
            else:
                res[nums[i]] += 1
        for k, v in res.items():
            if v == 1:
                return k


# Mathmatical computation
# [a, a, c, b, c]: 2*(a+b+c) - (a+a+c+b+c) = b
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


# Bit Manipulation
# use XOR. a ^ a = 0 and a ^ 0 = a
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for item in nums:
            a ^= item
        return a
