# Count and Say
#
# [Easy] [AC:44.2% 394.6K of 893K] [filetype:python3]
#
# The count-and-say sequence is the sequence of integers with the
# first five terms as following:
#
# 1.     1
#
# 2.     11
#
# 3.     21
#
# 4.     1211
#
# 5.     111221
#
# 1 is read off as "one 1" or 11.
#
# 11 is read off as "two 1s" or 21.
#
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the
# count-and-say sequence. You can do so recursively, in other words
# from the previous member read off the digits, counting the number of
# digits in groups of the same digit.
#
# Note: Each term of the sequence of integers will be represented as
# a string.
#
# Example 1:
#
# Input: 1
#
# Output: "1"
#
# Explanation: This is the base case.
#
# Example 2:
#
# Input: 4
#
# Output: "1211"
#
# Explanation: For n = 3 the term was "21" in which we have two groups
# "2" and "1", "2" can be read as "12" which means frequency = 1 and
# value = 2, the same way "1" is read as "11", so the answer is the
# concatenation of "12" and "11" which is "1211".
#
# [End of Description]:
# Sliding Window
class Solution:
    def countAndSay(self, n: int) -> str:
        return "".join(self.nextSequence(n, ["1", "E"]))

    def nextSequence(self, n, prevSeq):
        if n == 1:
            return prevSeq[:-1]

        print(f"n is {n}, prevSeq is {prevSeq}")
        nextSeq = []
        preDigit = prevSeq[0]
        digitcnt = 1
        for digit in prevSeq[1:]:
            if digit == preDigit:
                digitcnt += 1
            else:
                nextSeq.extend([str(digitcnt), preDigit])
                preDigit = digit
                digitcnt = 1
        nextSeq.append("E")
        print(f"before rerutn, nextSeq is {nextSeq}")
        return self.nextSequence(n - 1, nextSeq)


if __name__ == "__main__":
    print(Solution().countAndSay(5))
