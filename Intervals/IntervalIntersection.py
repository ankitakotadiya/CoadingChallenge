'''
# To solve this problem two pointer technique can be used.
# Maintain a two pointer i and j to traverse two interval lists.
# Now find insersection between first interval of both list. This can be done by, if second list's interval start just before first.
# Intersection point can be calculated max value of both of start point and min value of both of end point.
# Increment i and j pointer accordingly to move ahead.
# If first interval's end is greater then first interval might intersect with secondlist's second interval so increment j by one else increment i.

Time Complexity: O(n+m), where n+m is the length of both lists.
Space Complexity: O(1)

'''

'''
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
'''

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        i , j = 0,0
        result = []
        
        while i < len(firstList) and j < len(secondList):
            si,ei = firstList[i]
            sj,ej = secondList[j]
            
            if si <= ej and sj <= ei:
                result.append((max(si,sj),min(ei,ej)))
                
            if ei > ej:
                j+=1
            
            elif :
                i+=1
                
        return result
