# Valid Palindrome
#
# [Easy] [AC:35.6% 577.2K of 1.6M] [filetype:python3]
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
#
# Example 1:
#
# Input: "A man, a plan, a canal: Panama"
#
# Output: true
#
# Example 2:
#
# Input: "race a car"
#
# Output: false
#
# Constraints:
#
# s consists only of printable ASCII characters.
#
# [End of Description]:
# two poiners
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if i < j and s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
        return True
