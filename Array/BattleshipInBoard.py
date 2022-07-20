class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        
        n = len(board)
        count = 0
        
        for i in range(n):
            
            for j in range(len(board[i])):
                
                if board[i][j] == 'X':
                    
                    if (i - 1 >= 0 and board[i-1][j] == 'X') or (j-1 >= 0 and board[i][j-1] == 'X'):
                        continue
                    
                    count+=1
                    
        return count
