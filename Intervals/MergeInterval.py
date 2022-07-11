class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        i, j = 0, 1
        intervals.sort()
        
        while j < len(intervals):
            
            if intervals[i][1] >= intervals[j][0]:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                s = intervals.pop(j)
            else: 
                i+=1
                j+=1
        
        return intervals
