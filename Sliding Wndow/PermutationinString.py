class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_d={}
        s2_d={}
        l = 0
        
        for x in s1:
            s1_d[x] = s1_d.get(x,0)+1
        
        for r,val in enumerate(s2):
            s2_d[val] = s2_d.get(val,0)+1
            
            if s1_d == s2_d:
                return True
            
            if r >= len(s1)-1:
                if s2_d[s2[l]] == 1:
                    del s2_d[s2[l]]
                
                else:
                    s2_d[s2[l]] -= 1
                
                l+=1
        return False
