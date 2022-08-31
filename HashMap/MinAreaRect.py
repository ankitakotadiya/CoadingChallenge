'''
You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
'''

'''
# Will start to visit each pair of coordination and search in visited set if their neighbours exist or not if yes then it will form a rectangle, will calculate area which form minimum rect and save in our minimum variable.
# Will do the same process for each pair if any minimum rect then previous store in such case only update minimum area else at the end return minimum rectangle area.

Time Complexity:O(n*n)
Space Complexity: O(n)
'''

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        visited = set()
        min_size = float('inf')
        
        for x1,y1 in points:
            
            for x2,y2 in visited:
                
                if (x1,y2) in visited and (x2,y1) in visited:
                    
                    area = abs(x2-x1) * abs(y2-y1)
                    min_size = min(min_size,area)
                    
            visited.add((x1,y1))
            
        if min_size == float('inf'):
            return 0
        else:
            return min_size
