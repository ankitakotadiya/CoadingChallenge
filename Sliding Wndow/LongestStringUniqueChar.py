'''
# Initialise left and right pointer equal to 0.
# Initialise an array to store the characters of the current window. This array always store unique characters.
# Move right pointer towards N, where N is the of the array.
# Till this right point we have maximum non repeating substring length. Store that length of substring to the result in each iteration.
# If a character is found, which is present in the array then remove that character and append current character.
# Follow the process to the end of the character and return maximum size of substring.

Time Complexity: O(n)
Space Complexity: O(m), where m is length of the unique character.
'''

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
