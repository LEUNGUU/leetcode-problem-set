# Valid Parentheses
#
# [Easy] [AC:38.5% 967.9K of 2.5M] [filetype:python3]
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
#
# Open brackets must be closed in the correct order.
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
#
# Output: true
#
# Example 2:
#
# Input: "()[]{}"
#
# Output: true
#
# Example 3:
#
# Input: "(]"
#
# Output: false
#
# Example 4:
#
# Input: "([)]"
#
# Output: false
#
# Example 5:
#
# Input: "{[]}"
#
# Output: true
#
# [End of Description]:
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for item in s:
            if item in "({[":
                stack.append(item)
            elif item in "]})":
                if stack:
                    opening_bracket = stack.pop()
                    if parentheses_map[opening_bracket] != item:
                        return False
                else:
                    return False
        if not stack:
            return True
        else:
            return False
