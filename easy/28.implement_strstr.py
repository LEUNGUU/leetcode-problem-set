# Implement strStr()
#
# [Easy] [AC:34.2% 642.2K of 1.9M] [filetype:python3]
#
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
#
# Output: 2
#
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
#
# Output: -1
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
#
# [End of Description]:
# My own solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenOfneedle = len(needle)
        if lenOfneedle == 0:
            return 0
        else:
            index = 0
            while (index + lenOfneedle) <= len(haystack):
                if haystack[index : index + lenOfneedle] == needle:
                    return index
                index += 1
            return -1


# Substring: Linear Time slice
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start : start + L] == needle:
                return start
        return -1


# Two Pointers: Linear Time Slice
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)
        if L == 0:
            return 0
        pn = 0
        while pn < n - L + 1:
            # find the position of the first needle character
            # in the haystack string
            while pn < n - L + 1 and haystack[pn] != needle[0]:
                pn += 1
            # compute the max match string
            curr_len = pL = 0
            while pL < L and pn < n and haystack[pn] == needle[pL]:
                pn += 1
                pL += 1
                curr_len += 1
            # if the whole needle string is found,
            # return its start position
            if curr_len == L:
                return pn - L
            # otherwise, backtrack
            pn = pn - curr_len + 1
        return -1


# Rabin Karp: Constant Time Slice
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)
        if L > n:
            return -1
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2 ** 31
        # lambda-function to convert character to integer
        h_to_int = lambda i: ord(haystack[i]) - ord("a")
        needle_to_int = lambda i: ord(needle[i]) - ord("a")
        # compute the hash of strings haystack[:L], needle[:L]
        h = ref_h = 0
        for i in range(L):
            h = (h * a + h_to_int(i)) % modulus
            ref_h = (ref_h * a + needle_to_int(i)) % modulus
        if h == ref_h:
            return 0
        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - h_to_int(start - 1) * aL + h_to_int(start + L - 1)) % modulus
            if h == ref_h:
                return start

        return -1
