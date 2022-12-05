# Find All Anagrams in a String
#
# [Medium] [AC:43.7% 295.4K of 676.3K] [filetype:python3]
#
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than
# 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
#
# s: "cbaebabacd" p: "abc"
#
# Output:
#
# [0, 6]
#
# Explanation:
#
# The substring with start index = 0 is "cba", which is an anagram of "abc".
#
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
# Example 2:
#
# Input:
#
# s: "abab" p: "ab"
#
# Output:
#
# [0, 1, 2]
#
# Explanation:
#
# The substring with start index = 0 is "ab", which is an anagram of "ab".
#
# The substring with start index = 1 is "ba", which is an anagram of "ab".
#
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
# [End of Description]:
from collections import Counter, defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        window = defaultdict(int)

        left = right = 0
        valid = 0
        res = []

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # due to testcase 'baa', 'aa'
            # we change len(need) to len(p)
            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res
