from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slowV2 = 0
        while True:
            slow = nums[slow]
            slowV2 = nums[slowV2]
            if slow == slowV2:
                break

        return slow
