'''
# This problem can be solved by two pointer.
# First sort the intervals.
# Initially set point i at 0 index and pointer j at index 1.
# Now check if there is intersection between interval at 0 index and interval at index 1 then simply merge two interval and remove interval at index 1.
# Again check two intervals if no intersection then increment both the pointers.
# Follow the process until second pointer is less than the length of interval list.

Time Complexity: O(nLogn)
Space Complexity: O(1)
'''

'''
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
'''
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
