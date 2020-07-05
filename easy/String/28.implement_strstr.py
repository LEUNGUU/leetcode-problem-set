# Implement strStr()
#
# [Easy] [AC:34.2% 642.2K of 1.9M] [filetype:python3]
#
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
#
# Output: 2
#
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
#
# Output: -1
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
#
# [End of Description]:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenOfneedle = len(needle)
        if lenOfneedle == 0:
            return 0
        else:
            index = 0
            while (index + lenOfneedle) <= len(haystack):
                if haystack[index : index + lenOfneedle] == needle:
                    return index
                index += 1
            return -1
