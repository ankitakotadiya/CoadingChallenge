class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if len(grid) == 0 or grid is None:
            return 0
        
        island = 0
        
        for i in range(len(grid)):
            
            for j in range(len(grid[i])):
                
                if grid[i][j] == '1':
                    self.dfs(i,j,grid)
                    island+=1
                    
        return island
                    
    def dfs(self,i,j,grid):
        
        grid[i][j] = 'X'
        print(grid)
        
        if i-1 >= 0 and grid[i-1][j] == '1':
            self.dfs(i-1,j,grid)
        
        if j-1 >= 0 and grid[i][j-1] == '1':
            self.dfs(i,j-1,grid)
            
        if i+1 < len(grid) and grid[i+1][j] == '1':
            self.dfs(i+1,j,grid)
            
        if j+1 < len(grid[0]) and grid[i][j+1] == '1':
            self.dfs(i,j+1,grid)
