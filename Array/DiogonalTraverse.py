class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        
        def isbound(i,j,m,n):
            
            return i < 0 or j<0 or i > m or j > n
        
        i,j = 0,0
        m,n = len(mat) - 1, len(mat[0]) - 1
        res = []
        goingup = True
        
        while not isbound(i,j,m,n):
            
            res.append(mat[i][j])
            
            if goingup:
                
                if i == 0 or j == n:
                    goingup = False
                    
                    if j == n:
                        i+=1
                    else:
                        j+=1
                else:
                    i-=1
                    j+=1
                    
            else:
                
                if j == 0 or i == m:
                    
                    goingup = True
                    if i == m:
                        j+=1
                    else:
                        i+=1
                        
                else:
                    i+=1
                    j-=1
                    
        return res
