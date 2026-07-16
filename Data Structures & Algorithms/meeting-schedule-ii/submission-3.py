"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda i: i.start)
        res = 1
        endTimes = []
        heapq.heappush(endTimes, intervals[0].end)
        
        for i in range(1, len(intervals)):
            smallest = endTimes[0]
            if intervals[i].start < smallest:
                res += 1
            else:
                heapq.heappop(endTimes)
            heapq.heappush(endTimes, intervals[i].end)
        return res
            



        