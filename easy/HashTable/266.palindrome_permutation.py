# Palindrome Permutation
#
# [Easy] [AC:61.9% 92.4K of 149.3K] [filetype:python3]
#
# Given a string, determine if a permutation of the string could form a palindrome.
#
# Example 1:
#
# Input: "code"
#
# Output: false
#
# Example 2:
#
# Input: "aab"
#
# Output: true
#
# Example 3:
#
# Input: "carerac"
#
# Output: true
#
# [End of Description]:
# from collections import Counter
#
# class Solution:
#     def canPermutePalindrome(self, s: str) -> bool:
#         countmap = Counter(s)
#         count = 0
#         for item in countmap.values():
#             count += item % 2
#         return count <= 1
from collections import defaultdict

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        countmap = defaultdict(int)
        count = 0
        for item in s:
            countmap[item] += 1
            if countmap[item] % 2 == 0:
                count -= 1
            else:
                count += 1
        return count <= 1

