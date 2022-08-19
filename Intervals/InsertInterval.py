'''
'''

'''
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()
        
        i,j = 0,1
        
        while j < len(intervals):
            
            if intervals[i][1] >= intervals[j][0]:
                intervals[i][1] = max(intervals[i][1],intervals[j][1])
                intervals.pop(j)
                
            else:
                i+=1
                j+=1
                
        return intervals
