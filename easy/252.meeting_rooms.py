# Meeting Rooms
#
# [Easy] [AC:54.4% 135.3K of 248.7K] [filetype:python3]
#
# Given an array of meeting time intervals consisting of start and end
# times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could
# attend all meetings.
#
# Example 1:
#
# Input: [[0,30],[5,10],[15,20]]
#
# Output: false
#
# Example 2:
#
# Input: [[7,10],[2,4]]
#
# Output: true
#
# NOTE: input types have been changed on April 15, 2019. Please reset
# to default code definition to get new method signature.
#
# [End of Description]:
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
