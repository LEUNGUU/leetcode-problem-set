# Permutations
#
# [Medium] [AC:64.2% 657.2K of 1M] [filetype:python3]
#
# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
#
# Output:
#
# [
#
#   [1,2,3],
#
#   [1,3,2],
#
#   [2,1,3],
#
#   [2,3,1],
#
#   [3,1,2],
#
#   [3,2,1]
#
# ]
#
# [End of Description]:
from copy import deepcopy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums: List[int], track: List[int]):
            # check if it is ended
            if len(nums) == len(track):
                # since track is reference, make a copy of track to avoid chaning the res
                copyOftrack = deepcopy(track)
                res.append(copyOftrack)

            for item in nums:
                if item in track:
                    continue
                track.append(item)
                backtrack(nums, track)
                track.pop()

        track = []
        res = []
        backtrack(nums, track)
        return res
