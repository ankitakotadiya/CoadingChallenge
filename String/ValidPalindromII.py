'''
# We can solve this problem by finding a position of mismatch.
# Will use two pointer to find mismatch.
# Set left pointer at 0 index and right at last index.
# keep increase both the pointers if left and right character are matched.
# Iteration will stop if we find mismatch character.
# We have traversed equal number of steps from both the side so after removing one character string should be palindrom.
# So will remove one char from left substring and append right substring.
# Same will remove one char from right substring append it to left substring.
# If one of them is palindrom then we can make palindrom after removing one char.
# If both substrings are not palindrom then it is not possible to make palindrom under given constraint.

Time Complexity: O(n)
Space Complexity: O(1)
'''

'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if s == s[::-1]:
            return True
        
        l = 0
        r = len(s)-1
        
        while l < r:
            
            if s[l] != s[r]:
                
                leftstring = s[:l] + s[l+1:]
                rightstring = s[:r]+s[r+1:]
                
                return leftstring == leftstring[::-1] or rightstring == rightstring[::-1]
            
            l+=1
            r-=1
        return True
