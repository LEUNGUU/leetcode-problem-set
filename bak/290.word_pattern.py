# Word Pattern
#
# [Easy] [AC:37.0% 193.8K of 523.8K] [filetype:python3]
#
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in
# str.
#
# Example 1:
#
# Input: pattern = "abba", str = "dog cat cat dog"
#
# Output: true
#
# Example 2:
#
# Input:pattern = "abba", str = "dog cat cat fish"
#
# Output: false
#
# Example 3:
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
#
# Output: false
#
# Example 4:
#
# Input: pattern = "abba", str = "dog dog dog dog"
#
# Output: false
#
# Notes:
#
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by
# a single space.
#
# [End of Description]:
# Two Hash Maps
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        charMap = {}
        wordMap = {}

        words = str.split(" ")
        if len(words) != len(pattern):
            return False

        for c, w in zip(pattern, words):
            if c not in charMap:
                if w in wordMap:
                    return False
                else:
                    charMap[c] = w
                    wordMap[w] = c
            else:
                if charMap[c] != w:
                    return False
        return True


# Single Index Hash Map
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map_index = {}
        words = str.split()

        if len(pattern) != len(words):
            return False

        for index in range(len(words)):
            p = pattern[index]
            w = words[index]

            p_key = "pattern_{}".format(p)
            w_key = "word_{}".format(w)

            if p_key not in map_index:
                map_index[p_key] = index

            if w_key not in map_index:
                map_index[w_key] = index

            if map_index[p_key] != map_index[w_key]:
                return False
        return True
