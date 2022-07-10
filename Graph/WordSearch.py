class Solution:
    
    def dfs(self,word,k,i,j,visited,board):
        
        if k == len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[k]:
            return False
        
        visited[i][j] = True
        res1 = self.dfs(word,k+1,i+1,j,visited,board)
        res2 = self.dfs(word,k+1,i-1,j,visited,board)
        res3 = self.dfs(word,k+1,i,j-1,visited,board)
        res4 = self.dfs(word,k+1,i,j+1,visited,board)
        
        visited[i][j] = False
        print(visited,end='\n')
        return res1 or res2 or res3 or res4
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        newstr = ''
        arr = list(word)
        for i in range(len(board)):
            
            for j in range(len(board[i])):
                
                k = 0
                visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                if self.dfs(word,k,i,j,visited,board):
                    return True
