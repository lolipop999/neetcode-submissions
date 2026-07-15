class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        end = newInterval[1]
        for i, interval in enumerate(intervals):
            if interval[0] > end:
                # insert newInterval at index i
                intervals.insert(i, newInterval)
                return intervals
            elif newInterval[0] <= interval[1]:
                if newInterval[0] < interval[0]:
                    interval[0] = newInterval[0]
                for j in range(i, len(intervals)):
                    if end < intervals[j][0]:
                        intervals[i][1] = end
                        del intervals[i+1:j]
                        return intervals
                    if end <= intervals[j][1]:
                        intervals[i][1] = intervals[j][1]
                        del intervals[i+1:j+1]
                        return intervals
                intervals[i][1] = end
                del intervals[i+1:]
                return intervals
        intervals.append(newInterval)
        return intervals        