class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charset = []
        maxarea = 0
        
        if len(s) == 1:
            return 1
        
        for i in range(len(s)):
            
            if s[i] in charset:
                
                indx = charset.index(s[i])
                charset = list(charset[indx+1:len(charset)])
                charset.append(s[i])
                
            else:
                charset.append(s[i])
                
            maxarea = max(maxarea,len(charset))
        
        return maxarea
