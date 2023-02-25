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
# Not quite safe
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         return int(sqrt(x))


# a mathmatics method
# sqrt(x) = e** (1/2) * log(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = int(e ** (0.5 * log(x)))
        right = left + 1

        return left if right * right > x else right


# Recursion and Bits Shifts
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = self.mySqrt(x >> 2) << 1
        right = left + 1

        return left if right * right > x else right


# we use binary search here
# For x ≥ 2 the square root is always smaller than x/2 and larger than 0 : 0 < a < x/2.
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 2, x // 2
        while left <= right:
            pivot = (left + right) // 2
            if pivot * pivot > x:
                # we should move right pointer to left
                right = pivot - 1
            elif pivot * pivot < x:
                # we should move left pointer to right
                left = pivot + 1
            else:
                # we found the exact value
                return pivot
        # because when left larger than right, right is the floor of sqrt(x), then we return right
        return right
