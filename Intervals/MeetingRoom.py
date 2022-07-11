class Solution:
  def meetingRoom(self,intervals):
    
    intervals.sort()
    
    i,j = 0,1
    room = 1
    while(j < len(intervals):
          
          if intervals[i][0] < intervals[j][1] and intervals[j][0] < intervals[i][1]:
            room+=2
          else:
            i+=1
            j+=1
          
    return room
            
            
            
          
