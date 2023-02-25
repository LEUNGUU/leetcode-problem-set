# Pascal's Triangle
#
# [Easy] [AC:51.7% 373K of 720.9K] [filetype:python3]
#
# Given a non-negative integer numRows, generate the first numRows of
# Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers
# directly above it.
#
# Example:
#
# Input: 5
#
# Output:
#
# [
#
#      [1],
#
#     [1,1],
#
#    [1,2,1],
#
#   [1,3,3,1],
#
#  [1,4,6,4,1]
#
# ]
#
# [End of Description]:


# Dynamic Programming
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row_num in range(numRows):
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1
            # when len(row) - 1 <= 1, this loop will not execute.
            # It means range(1, 0) and rnage(1, 1) is null
            for j in range(1, len(row) - 1):
                # f(n) = f(n-1) + f(n-2)
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            triangle.append(row)
        return triangle
