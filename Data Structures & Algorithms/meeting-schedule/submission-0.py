"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from operator import attrgetter
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #start of one cannot be less than the end of another
        # first sort based on start time
        sorted_times = sorted(intervals, key=attrgetter("start"))
        
        available = 0
        for meeting in sorted_times:
            if meeting.start < available:
                return False
            available = meeting.end
        return True