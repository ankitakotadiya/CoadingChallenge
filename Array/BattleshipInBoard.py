'''
# Run through loop of rows and column and iterate element placed in a cell.
# If element equal to the 'X' which represent the battleship then simply check it's adjacent element if found any battleship then simply continue to next element otherwise increase the count by one.
# At the end return number of battleship in the board.

Time Complexity: O(n*m) n is number of rows, m is number of column.
Space Complexity: O(1)
'''

'''
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.
Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
'''

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
