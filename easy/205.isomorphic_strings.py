# Isomorphic Strings
#
# [Easy] [AC:39.6% 291.8K of 736.9K] [filetype:python3]
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced
# to get t.
#
# All occurrences of a character must be replaced with another
# character while preserving the order of characters. No two
# characters may map to the same character but a character may map to
# itself.
#
# Example 1:
#
# Input: s = "egg", t = "add"
#
# Output: true
#
# Example 2:
#
# Input: s = "foo", t = "bar"
#
# Output: false
#
# Example 3:
#
# Input: s = "paper", t = "title"
#
# Output: true
#
# Note:
#
# You may assume both s and t have the same length.
#
# [End of Description]:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alph = {}
        for i in range(len(s)):
            # first we need to check if s[i] already in alph
            if s[i] in alph.keys():
                # s[i] in alph, then we need to check if t[i] matches its value
                # we cannot make it an 'and' condition
                if alph[s[i]] != t[i]:
                    return False
            # s[i] not in alph, then before we add it to alph, we need to confirm t[i] is not in alph
            elif t[i] in list(alph.values()):
                return False
            else:
                alph[s[i]] = t[i]
        return True
