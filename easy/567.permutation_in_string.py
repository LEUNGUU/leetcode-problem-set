# Permutation in String
#
# [Medium] [AC:44.4% 148.5K of 334.2K] [filetype:python3]
#
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one
# of the first string's permutations is the substring of the second string.
#
# Example 1:
#
# Input: s1 = "ab" s2 = "eidbaooo"
#
# Output: True
#
# Explanation: s2 contains one permutation of s1 ("ba").
#
# Example 2:
#
# Input:s1= "ab" s2 = "eidboaoo"
#
# Output: False
#
# Constraints:
#
# The input strings only contain lower case letters.
#
# The length of both given strings is in range [1, 10,000].
#
# [End of Description]:
from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = defaultdict(int)

        left = right = 0
        valid = 0

        while right < len(s2):
            c = s2[right]
            right += 1

            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # this is the size of sliding window
            while right - left >= len(s1):
                if valid == len(need):
                    return True
                d = s2[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False
