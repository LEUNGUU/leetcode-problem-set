from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            target_value = target - value
            if target_value in hashmap.keys():
                return [hashmap[target_value], index]
            hashmap[value] = index
        return []
