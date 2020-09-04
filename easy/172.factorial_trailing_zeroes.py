# Factorial Trailing Zeroes
#
# [Easy] [AC:37.7% 207.4K of 549.7K] [filetype:python3]
#
# Given an integer n, return the number of trailing zeroes in n!.
#
# Example 1:
#
# Input: 3
#
# Output: 0
#
# Explanation: 3! = 6, no trailing zero.
#
# Example 2:
#
# Input: 5
#
# Output: 1
#
# Explanation: 5! = 120, one trailing zero.
#
# Note: Your solution should be in logarithmic time complexity.
#
# [End of Description]:
# brute force(cannot submit due to timeout)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            res = math.factorial(n)
            times = 0
            while res > 0:
                if (res % 10) != 0:
                    break
                times += 1
                res //= 10
            return times


class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        multipler = 5
        while n >= multipler:
            cnt += n // multipler
            multipler *= 5
        return cnt
