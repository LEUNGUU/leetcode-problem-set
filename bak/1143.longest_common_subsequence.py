# Longest Common Subsequence
#
# [Medium] [AC:58.4% 139K of 238K] [filetype:python3]
#
# Given two strings text1 and text2, return the length of their longest common subsequence.
#
# A subsequence of a string is a new string generated from the original string with some
# characters(can be none) deleted without changing the relative order of the
# remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is
# not). A common subsequence of two strings is a subsequence that is common to both strings.
#
# If there is no common subsequence, return 0.
#
# Example 1:
#
# Input: text1 = "abcde", text2 = "ace"
#
# Output: 3
#
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
# Example 2:
#
# Input: text1 = "abc", text2 = "abc"
#
# Output: 3
#
# Explanation: The longest common subsequence is "abc" and its length is 3.
#
# Example 3:
#
# Input: text1 = "abc", text2 = "def"
#
# Output: 0
#
# Explanation: There is no such common subsequence, so the result is 0.
#
# Constraints:
#
# 1 <= text1.length <= 1000
#
# 1 <= text2.length <= 1000
#
# The input strings consist of lowercase English characters only.
#
# [End of Description]:
# memo
# key point is creating the dp array
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dp(i, j):
            # base case
            if i == -1 or j == -1:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if text1[i] == text2[j]:
                # find the common character
                memo[(i, j)] = dp(i - 1, j - 1) + 1
                return memo[(i, j)]
            else:
                memo[(i, j)] = max(dp(i - 1, j), dp(i, j - 1))
                return memo[(i, j)]

        return dp(len(text1) - 1, len(text2) - 1)
