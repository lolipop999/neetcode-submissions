class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals first
        intervals.sort(key = lambda i: i[0])

        res = 0
        if intervals:
            prev = intervals[0]
        else:
            return 0
        
        for i in range(1, len(intervals)):
            if prev[1] > intervals[i][0]:
                res += 1
                prev[1] = min(prev[1], intervals[i][1])
            else:
                prev[1] = intervals[i][1]
        return res