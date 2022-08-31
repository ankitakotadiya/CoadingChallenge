'''
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

'''

'''
# Run through loop from start to end.
# In each iteration find difference of string as key store in hashmap as key(Let's sat for string acd key is 21) and value as current element.
# In next iteration if we get same key that means current string fall into same group so will append string against same key.
# At the end return all values of hashmap.

Time Complexity: O(n*k), n number of strings and k is the length of loggest string.
Space Complexity: O(n)
'''

class Solution:
  
  def geoupString(self,str):
    
    dic = defaultdict(list)
    
    def getkey(s):
      
      key = ''
      
      for i in range(1,len(s)):
        
        diff = (ord(s[i] - ord(s[i-1]) + 26) % 26
        key += diff
                
      return key
                
    for i in str:
      dic[getkey(i)].append(i)
                
    return dic.values()
                
