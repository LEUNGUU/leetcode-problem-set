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
        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        parentheses_map = {"(": ")", "[": "]", "{": "}"}
        # the stack to keep track of opening brackets
        stack = []
        # for every bracket in the expression
        for item in s:
            # if the characters is an closing bracket
            if item in "({[":
                stack.append(item)
            elif item in "]})":
                if stack:
                    opening_bracket = stack.pop()
                    if parentheses_map[opening_bracket] != item:
                        return False
                else:
                    return False
        return not stack
