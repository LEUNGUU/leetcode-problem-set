# Valid Anagram
#
# [Easy] [AC:56.5% 568.8K of 1M] [filetype:python3]
#
# Given two strings s and t , write a function to determine if t is an
# anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
#
# Output: true
#
# Example 2:
#
# Input: s = "rat", t = "car"
#
# Output: false
#
# Note:
#
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
#
# What if the inputs contain unicode characters? How would you adapt
# your solution to such case?
#
# [End of Description]:

# Hashmap
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = defaultdict(int)
        for item in s:
            hashmap[item] += 1
        for item in t:
            hashmap[item] -= 1
            if hashmap[item] < 0:
                return False
        return True
