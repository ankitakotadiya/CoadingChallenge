'''
# First sort the invervals.
# Intially assign room = 1 because for first interval you need one room.
# Now check interval 1 and interval two, if current start is less than the previous interval's end that means there is overlap and you need a separate room so increase room count by one.
# Run through loop and at the end return number of rooms required.

Time Complexity: O(nLogn)
Space Complexity: O(1)
'''

'''
Number of rooms required to attend all the meetings.
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
'''

class Solution:
  def meetingRoom(self,intervals):
    
    intervals.sort()
    
    room = 1
    lastend = intervals[0][1]

    for i in range(1,len(intervals)):
      start,end = intervals[i]
      
      if lastend > start:
        room += 1
        
      lastend = end

    return room
            
            
            
          
