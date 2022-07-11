class Solution:
    def mySqrt(self, x: int) -> int:
        
        s = 0
        e = x
        
        while s <= e:
            
            mid = (s+e)//2
            
            mul = mid*mid
            
            if mul == x:
                return mid
            elif mul < x:
                s = mid+1
            else:
                e = mid-1
                
        return e
