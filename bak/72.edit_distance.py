# Edit Distance
#
# [Hard] [AC:45.4% 302.7K of 666.6K] [filetype:python3]
#
# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
#
# Delete a character
#
# Replace a character
#
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
#
# Output: 3
#
# Explanation:
#
# horse -> rorse (replace 'h' with 'r')
#
# rorse -> rose (remove 'r')
#
# rose -> ros (remove 'e')
#
# Example 2:
#
# Input: word1 = "intention", word2 = "execution"
#
# Output: 5
#
# Explanation:
#
# intention -> inention (remove 't')
#
# inention -> enention (replace 'i' with 'e')
#
# enention -> exention (replace 'n' with 'x')
#
# exention -> exection (replace 'n' with 'c')
#
# exection -> execution (insert 'u')
#
# [End of Description]:
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = dict()

        def dp(i, j):
            # base case
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1

            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)
            else:
                memo[(i, j)] = min(
                    dp(i - 1, j) + 1, dp(i - 1, j - 1) + 1, dp(i, j - 1) + 1
                )
            return memo[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)
