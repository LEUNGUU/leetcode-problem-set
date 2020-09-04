# Power of Three
#
# [Easy] [AC:42.1% 272.3K of 647.3K] [filetype:python3]
#
# Given an integer, write a function to determine if it is a power of three.
#
# Example 1:
#
# Input: 27
#
# Output: true
#
# Example 2:
#
# Input: 0
#
# Output: false
#
# Example 3:
#
# Input: 9
#
# Output: true
#
# Example 4:
#
# Input: 45
#
# Output: false
#
# Follow up:
#
# Could you do it without using any loop / recursion?
#
# [End of Description]:

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while (n % 3) == 0:
            n /= 3
        return n == 1


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        bigger = math.pow(3, 20)
        return n > 0 and bigger % n == 0
