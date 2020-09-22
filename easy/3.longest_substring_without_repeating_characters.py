# Longest Substring Without Repeating Characters
#
# [Medium] [AC:30.6% 1.7M of 5.6M] [filetype:python3]
#
# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
#
# Output: 3
#
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
# Input: s = "bbbbb"
#
# Output: 1
#
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#
# Input: s = "pwwkew"
#
# Output: 3
#
# Explanation: The answer is "wke", with the length of 3.
#
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Example 4:
#
# Input: s = ""
#
# Output: 0
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
#
# s consists of English letters, digits, symbols and spaces.
#
# [End of Description]:
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)

        left = right = 0
        res = 0

        while right < len(s):
            c = s[right]
            right += 1

            window[c] += 1
            # remove values based on the amount of repeated numbers
            while window[c] > 1:
                d = s[left]
                left += 1

                window[d] -= 1
            res = max(res, right - left)
        return res
