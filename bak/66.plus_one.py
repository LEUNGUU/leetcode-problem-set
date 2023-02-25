# Plus One
#
# [Easy] [AC:42.2% 590.5K of 1.4M]
# [filetype:python3]
#
# Given a non-empty array of digits
# representing a non-negative integer, plus
# one to the integer.
#
# The digits are stored such that the most
# significant digit is at the head of the
# list, and each element in the array contain
# a single digit.
#
# You may assume the integer does not contain
# any leading zero, except the number
# 0 itself.
#
# Example 1:
#
# Input: [1,2,3]
#
# Output: [1,2,4]
#
# Explanation: The array represents the
# integer 123.
#
# Example 2:
#
# Input: [4,3,2,1]
#
# Output: [4,3,2,2]
#
# Explanation: The array represents the
# integer 4321.
#
# [End of Description]:


# Note that, a straightforward idea to convert everything
# into integers and then apply the addition could be risky,
# especially for the implementation in Java, due to the potential integer overflow issue.
# As one can imagine, once the array gets long,
# the result of conversion cannot fit into the data type of Integer,
# or Long, or even BigInteger.
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numbers = int("".join([str(item) for item in digits])) + 1
        return list(str(numbers))


# offical solution(Schoolbook Addition with Carry)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)

        for i in range(length):
            # start from the last element
            index = length - 1 - i
            if digits[index] == 9:
                digits[index] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1
                digits[index] += 1
                # and the job is done
                return digits
        # we are here because all the digits are nines
        return [1] + digits
