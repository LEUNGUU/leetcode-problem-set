# Length of Last Word
#
# [Easy] [AC:32.5% 371K of 1.1M] [filetype:python3]
#
# Given a string s consists of upper/lower-case alphabets and empty
# space characters ' ', return the length of last word (last word
# means the last appearing word if we loop from left to right) in the
# string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a maximal substring consisting of
# non-space characters only.
#
# Example:
#
# Input: "Hello World"
#
# Output: 5
#
# [End of Description]:
# My own solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        substr_list = s.split(" ")
        length = len(substr_list)
        for i in range(length - 1, -1, -1):
            if substr_list[i] != "":
                return len(substr_list[i])
        # null string
        return 0


# String Index Manipulation
class Solution:
    def lengthOfLastWord(self, s: str) -> str:
        # trim the trailing spaces
        length = len(s) - 1
        while length >= 0 and s[length] == " ":
            length -= 1

        # compute the length of last word
        result = 0
        while length >= 0 and s[length] != " ":
            length -= 1
            result += 1
        return result


# one-loop iteration
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length, result = len(s), 0
        while length > 0:
            length -= 1
            # we're in the middle of the last word
            if s[length] != " ":
                result += 1
            # here is the end of last word
            elif result > 0:
                return result
        return result
