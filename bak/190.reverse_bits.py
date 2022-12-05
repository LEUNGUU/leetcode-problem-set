# Reverse Bits
#
# [Easy] [AC:37.2% 251.6K of 676.9K]
# [filetype:python3]
#
# Reverse bits of a given 32 bits unsigned integer.
#
# Example 1:
#
# Input: 00000010100101000001111010011100
#
# Output: 00111001011110000010100101000000
#
# Explanation: The input binary string
# 00000010100101000001111010011100 represents the
# unsigned integer 43261596, so return 964176192
# which its binary representation is
# 00111001011110000010100101000000.
#
# Example 2:
#
# Input: 11111111111111111111111111111101
#
# Output: 10111111111111111111111111111111
#
# Explanation: The input binary string
# 11111111111111111111111111111101 represents the
# unsigned integer 4294967293, so return 3221225471
# which its binary representation is
# 10111111111111111111111111111111.
#
# Note:
#
# Note that in some languages such as Java, there
# is no unsigned integer type. In this case, both
# input and output will be given as signed integer
# type and should not affect your implementation,
# as the internal binary representation of the
# integer is the same whether it is signed or
# unsigned.
#
# In Java, the compiler represents the signed
# integers using 2's complement notation.
# Therefore, in Example 2 above the input
# represents the signed integer -3 and the output
# represents the signed integer -1073741825.
#
# Follow up:
#
# If this function is called many times, how would
# you optimize it?
#
# [End of Description]:
# Bit by Bit reverse
# The key idea is that for a bit that is situated at the index i, after the reversion, its
# position should be 31 - i (note: the index starts from zero)
#
# We iterate through the bit string of the input integer, from right to left (i.e. n = n >> 1).
# To retrieve the right-most bit of an integer, we apply the bit AND operation (n & 1).
#
# For each bit, we reverse it to the correct position (i.e. (n & 1) << power).
# Then we accumulate this reversed bit to the final result.
#
# When there is no more bits of one left (i.e. n == 0), we terminate the iteration.
class Solution:
    def reverseBits(self, n: int) -> int:
        res, power = 0, 31
        while n:
            res += (n & 1) << power
            n = n >> 1
            power -= 1
        return res


# Byte by Byte with Memorization
# We iterate over the bytes of an integer. To retrieve the right-most byte in an integer,
# again we apply the bit AND operation (i.e. n & 0xff) with the bit mask of 11111111.
#
# For each byte, first we reverse the bits within the byte,
# via a function called reverseByte(byte).
# Then we shift the reversed bits to their final positions.
#
# With the function reverseByte(byte),
# we apply the technique of memoization,
# which caches the result of the function and
# returns the result directly for the future invocations of the same input.
import functools


class Solution:
    def reverseBits(self, n: int) -> int:
        res, power = 0, 24
        while n:
            res += self.reverseByte(n & 0xFF) << power
            n = n >> 8
            power -= 8
        return res

    @functools.lru_cache(maxsize=256)
    def reverseByte(self, byte):
        return (byte * 0x0202020202 & 0x010884422010) % 1023
