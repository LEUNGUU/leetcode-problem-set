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
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            mid = len(strs) // 2
            leftstr = self.longestCommonPrefix(strs[0:mid])
            rightstr = self.longestCommonPrefix(strs[mid:])
            return self.CheckPrefix(leftstr, rightstr)

    def CheckPrefix(self, leftstr: str, rightstr: str) -> str:
        min_length = min(len(leftstr), len(rightstr))
        for index in range(min_length):
            if leftstr[index] != rightstr[index]:
                return leftstr[0:index]
        return leftstr[0:min_length]



