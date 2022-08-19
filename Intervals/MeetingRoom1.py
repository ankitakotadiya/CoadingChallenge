'''
# In this problem we just need to identify that if there is no overlap between meeting intervals then a person can attend all the meetings.
# For that sort intervals and run through loop and check current start time is less than the previous end time time that means no overlap.
# If this condition doesn't match then there is overlap and return False.
# Otherwise return True.

Time Complexity: O(nLogn)
Space Complexity: O(1)
'''

'''
Problem Statement: Check weather the person is able to all meetings then return True else False

Input: [[0,30],[5,10],[15,20]]
Output: False
'''

class Solution:
  
  def canAttendMeeting(self,intervals):
    
    intervals.sort()
    lastend = -1
    
    for start,end in intervals:
      
      if lastend < start:
        lastend = end
      else:
        return False
      
    return True
