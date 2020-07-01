# Two Sum III - Data structure design
#
# [Easy] [AC:33.3% 79.8K of 239.2K] [filetype:python3]
#
# Design and implement a TwoSum class. It should support the following
# operations: add and find.
#
# add - Add the number to an internal data structure.
#
# find - Find if there exists any pair of numbers which sum is equal to the
# value.
#
# Example 1:
#
# add(1); add(3); add(5);
#
# find(4) -> true
#
# find(7) -> false
#
# Example 2:
#
# add(3); add(1); add(2);
#
# find(3) -> true
#
# find(6) -> false
#
# [End of Description]:
class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._container = []
        self._isSorted = False

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        Time complexity is O(nlogn) timsort
        """
        self._container.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        Use two points to find two sums, time complexity is O(n)
        """
        if not self._isSorted:
            self._container.sort()
        pa, pb = 0, len(self._container) - 1
        while pa < pb:
            cur_sum = self._container[pa] + self._container[pb]
            if cur_sum > value:
                pb -= 1
            elif cur_sum < value:
                pa += 1
            else:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
