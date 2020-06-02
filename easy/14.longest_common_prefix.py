# Longest Common Prefix
#
# [Easy] [AC:35.1% 718.1K of 2M] [filetype:python3]
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
#
# Output: "fl"
#
# Example 2:
#
# Input: ["dog","racecar","car"]
#
# Output: ""
#
# Explanation: There is no common prefix among the input strings.
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#
# [End of Description]:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        else:
            min_length = len(strs[0])
            for item in strs[1:]:
                if len(item) < min_length:
                    min_length = len(item)
            start = 1
            while start <= min_length:
                mid = (start + min_length) // 2
                if self.CheckPrefix(strs, mid):
                    start = mid + 1
                else:
                    min_length = mid - 1
            return strs[0][0 : (start + min_length) // 2]

    def CheckPrefix(self, strs: List[str], lens: int) -> str:
        prefix = strs[0][0:lens]
        for item in strs:
            if not item.startswith(prefix):
                return False
        return True
