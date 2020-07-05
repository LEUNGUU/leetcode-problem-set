# Sqrt(x)
#
# [Easy] [AC:33.6% 544.8K of 1.6M] [filetype:python3]
#
# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be
# a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
#
# Example 1:
#
# Input: 4
#
# Output: 2
#
# Example 2:
#
# Input: 8
#
# Output: 2
#
# Explanation: The square root of 8 is 2.82842..., and since
#
#              the decimal part is truncated, 2 is returned.
#
# [End of Description]:
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         return int(sqrt(x))
# we use binary search here
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 2, x // 2
        while left <= right:
            pivot = (left + right) // 2
            if pivot * pivot > x:
                # we should move to left
                right = pivot - 1
            elif pivot * pivot < x:
                # we should move to right
                left = pivot + 1
            else:
                return pivot
        # because when left larger than right, right is the floor of sqrt(x), then we return right
        return right
