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

# hashmap defaultdict
# from collections import defaultdict
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         cnt = defaultdict(int)
#         for item in nums:
#             cnt[item] += 1
#         for k, v in cnt.items():
#             if v > (len(nums)/2):
#                 return k

# counter
# from collections import Counter
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         cnt = Counter(nums)
#         return max(cnt.keys(), key=cnt.get)

# sorting
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

