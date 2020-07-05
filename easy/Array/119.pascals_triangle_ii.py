# Pascal's Triangle II
#
# [Easy] [AC:48.4% 278.9K of 576.1K] [filetype:python3]
#
# Given a non-negative index k where k ≤ 33, return the kth index row
# of the Pascal's triangle.
#
# Note that the row index starts from 0.
#
# In Pascal's triangle, each number is the sum of the two numbers
# directly above it.
#
# Example:
#
# Input: 3
#
# Output: [1,3,3,1]
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#
# [End of Description]:
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for num_row in range(rowIndex + 1):
            row = [None for _ in range(num_row + 1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row) - 1):
                row[j] = triangle[num_row - 1][j - 1] + triangle[num_row - 1][j]
            triangle.append(row)
        return triangle[rowIndex]
