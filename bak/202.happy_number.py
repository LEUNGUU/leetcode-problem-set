# Happy Number
#
# [Easy] [AC:50.2% 508.7K of 1M] [filetype:python3]
#
# Write an algorithm to determine if a number n is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum
# of the squares of its digits, and repeat the process until the
# number equals 1 (where it will stay), or it loops endlessly in
# a cycle which does not include 1. Those numbers for which this
# process ends in 1 are happy numbers.
#
# Return True if n is a happy number, and False if not.
#
# Example:
#
# Input: 19
#
# Output: true
#
# Explanation:
#
# 12 + 92 = 82
#
# 82 + 22 = 68
#
# 62 + 82 = 100
#
# 12 + 02 + 02 = 1
#
# [End of Description]:

# Detect cycle with hashset(we use set here due to justify an element in set cost O(1))
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_next(n)
        return n == 1

    def get_next(self, n: int) -> int:
        total = 0
        while n > 0:
            n, digits = divmod(n, 10)
            total += digits**2
        return total


# two pointer
# we can therefore use Floyd's Cycle-Finding Algorithm here.
# This algorithm is based on 2 runners running around a circular race track,
# a fast runner and a slow runner. In reference to a famous fable,
# many people call the slow runner the "tortoise" and the fast runner the "hare".
class Solution:
    def isHappy(self, n: int) -> bool:
        slow_runner = n
        fast_runner = self.get_next(n)
        # while fast_runner != 1 and fast_runner != slow_runner:
        while fast_runner not in (1, slow_runner):
            slow_runner = self.get_next(slow_runner)
            fast_runner = self.get_next(self.get_next(fast_runner))
        return fast_runner == 1

    def get_next(self, n: int) -> int:
        total = 0
        while n > 0:
            n, digits = divmod(n, 10)
            total += digits**2
        return total
