'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Input: s = "loveleetcode"
Output: 2

'''

'''
# Here will use hashmap. Create a one empty hashmap.
# Go through all characters in string and save key as char and value as it's frequency in the hashmap.
# Agian iterate one by one char and search in hashmap, char has frequency = 1 if yes then break the loop and return index of that char.
# If frequency>1 then continue traversal else return -1.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        if not s:
            return -1
        
        dic = {}
        
        for c in s:
            
            if c not in dic:
                dic[c] = 1
            
            else:
                dic[c] += 1
                
                
        for i in range(len(s)):
            
            if dic[s[i]] == 1:
                return i
            
        return -1
