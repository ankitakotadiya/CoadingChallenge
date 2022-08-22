'''
# Traverse the matrix, each and island cell check any cell contains land then increase perimeter length by 4.
# Now check any adjacent cell contains land or not, If yes then minus perimeter length by 2 because adjacent cell connected through one common side and it has not been touched to water.
# Continue traverse all the cell and at the end return perimeter.

Time Complexity: O(n*m), n represents number of rows and m represents number of columns.
Space Complexity: O(1)
'''

'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
'''

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        P = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    P += 4
                    if i > 0 and grid[i - 1][j]:
                        P -= 2
                    if j > 0 and grid[i][j - 1]:
                        P -= 2
        return P
