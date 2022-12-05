# Add Binary
#
# [Easy] [AC:43.8% 442.5K of 1M] [filetype:python3]
#
# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
#
# Output: "100"
#
# Example 2:
#
# Input: a = "1010", b = "1011"
#
# Output: "10101"
#
# Constraints:
#
# Each string consists only of '0' or '1' characters.
#
# 1 <= a.length, b.length <= 10^4
#
# Each string is either "0" or doesn't contain any leading zero.
#
# [End of Description]:
# Bit-by-Bit Computation
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a, b = a.zfill(max_len), b.zfill(max_len)

        carry = 0
        result = []
        for i in range(max_len - 1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1

            if carry % 2 == 1:
                result.append("1")
            else:
                result.append("0")

            carry //= 2

        if carry == 1:
            result.append("1")
        result.reverse()

        return "".join(result)


# Bit Manipulation
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]
