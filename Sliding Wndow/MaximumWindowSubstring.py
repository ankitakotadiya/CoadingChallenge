'''
# First create a hash map that store character as key and frequency of character as value of substring.
# Now run the loop for second main string and store occerence of charactes in hash map. Increase the count if character match with substring.
# Once you reach count equal to the length of substring that means you have found window. 
# If such a window found then try to minimise the window by deleting character from the start of current window.
# If character at start in the current window already in substring then decrease count and again add new character in the window.
# Update minimum window size in the result.
# At the end return characters in the minimum window size.

Time Complexity: O(N)
Space Complexity: O(1)
'''


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
