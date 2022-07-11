def isBadVersion(version: int) -> bool:
    
    taget = 4
    
    if target == version:
        return True
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l = 1
        r = n
        mid = n//2
        
        while l <= r:
            
            
            
            if isBadVersion(mid):
                
                r = mid-1
                mid = (l+r)//2
            else:
                l = mid+1
                mid = (l+r)//2
                
        return mid+1
