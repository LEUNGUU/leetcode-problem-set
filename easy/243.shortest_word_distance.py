# Shortest Word Distance
#
# [Easy] [AC:60.8% 97.4K of 160.4K] [filetype:python3]
#
# Given a list of words and two words word1 and word2, return the shortest
# distance between these two words in the list.
#
# Example:
#
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Input: word1 = “coding”, word2 = “practice”
#
# Output: 3
#
# Input: word1 = "makes", word2 = "coding"
#
# Output: 1
#
# Note:
#
# You may assume that word1 does not equal to word2, and word1 and word2 are
# both in the list.
#
# [End of Description]:
# brute-force(Not Accepted)
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        minimum = len(words)
        for index1, item1 in enumerate(words):
            if item1 == word1:
                for index2, item2 in enumerate(words):
                    if item2 == word2:
                        minimum = min(minimum, abs(index1-index2))
        return minimum

# one-pass, every time pointer meets the words, we count and take the minimum so far.
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        minimum = len(words)
        i1 = i2 = -1
        for index, item in enumerate(words):
            if item == word1:
                i1 = index
            if item == word2:
                i2 = index
            if i1 != -1 and i2 != -1:
                minimum = min(minimum, abs(i1 - i2))
        return minimum
