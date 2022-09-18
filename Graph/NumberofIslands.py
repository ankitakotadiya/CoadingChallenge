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
        
        
        # print(grid)
        
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        
        grid[i][j] = 'X'
        self.dfs(i-1,j,grid)
        self.dfs(i,j-1,grid)
        self.dfs(i+1,j,grid)
        self.dfs(i,j+1,grid)
