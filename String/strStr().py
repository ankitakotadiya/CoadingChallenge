'''
# Run the loop from start of end.
# Here end is length of haystack - length of needle + 1.
# Each every index check whether the substring can be formed from that index or not, if yes then return that index.
# At the end of the loop if not found any substring then return -1.

Time Complexity: O(n)
Space Complexity: O(1)
'''

'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Input: haystack = "hello", needle = "ll"
Output: 2
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if not needle:
            return -1
        
        for i in range(0,len(haystack)-len(needle)+1):
            
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1
