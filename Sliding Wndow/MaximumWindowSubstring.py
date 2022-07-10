class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        charfreq = {}
        
        for char in t:
            
            if char in charfreq:
                charfreq[char] += 1
            else:
                charfreq[char] = 1
        
        matched = 0
        minstart = 0
        wstart = 0
        minlength = float('inf')
        
        for wend in range(len(s)):
            
            newchar = s[wend]
            
            if newchar in charfreq:
                charfreq[newchar] -= 1
            
                if charfreq[newchar] == 0:
                    matched += 1
            
            while matched == len(charfreq):
                
                windowsize = wend - wstart + 1
                
                if windowsize < minlength:
                    minlength = windowsize
                    minstart = wstart
                
                remove = s[wstart]
                
                if remove in charfreq:
                    
                    if charfreq[remove] == 0:
                        matched-=1
                    charfreq[remove]+=1
                wstart += 1
        if minlength == float('inf'):
            return ''
        return s[minstart:minstart+minlength]
