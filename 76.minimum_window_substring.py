# Minimum Window Substring
#
# [Hard] [AC:34.9% 430.7K of 1.2M] [filetype:python3]
#
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity
# O(n).
#
# Example:
#
# Input: S = "ADOBECODEBANC", T = "ABC"
#
# Output: "BANC"
#
# Note:
#
# If there is no such window in S that covers all characters in T, return the empty string "".
#
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
#
# [End of Description]:
# sliding window
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = defaultdict(int)
        need = Counter(t)

        left = right = 0
        valid = 0

        start = 0
        n = float("inf")

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if right - left < n:
                    start = left
                    n = right - left
                    print(n)

                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        print(f"left is {left}")
        print(f"n is {n}")
        return s[left : left + n]
