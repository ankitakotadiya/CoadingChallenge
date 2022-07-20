class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m//2):
            
            temp = matrix[i]
            matrix[i] = matrix[n-1-i]
            matrix[n-1-i] = temp
          
        for i in range(m):
            for j in range(i+1,n):
                
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
