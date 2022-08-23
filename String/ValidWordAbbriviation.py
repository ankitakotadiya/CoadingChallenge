'''
Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

Given s = "internationalization", abbr = "i12iz4n":
Return true.
'''

'''
# The approach is two pointer.
# Set abbriviation and word pointer initially 0.
# Now check value at abbr_pntr is digit, we need to handle case if it is 0 then return False because leading 0 is not allowed.
# If it is not zero then convert it to int move abbr_pntr by one check whether next char is digit or not, if yes, then add it step variable which stores abbriviation string's numeric value.
# We must move word pointer step times because number of steps characters are abbriviated.
# Now check next char if it is alpha and same in both the string then simply move both the pointer else return False.
# At the end of scanning if we get word_pnter == len(word) and abbr_pntr == len(abbr) then abbriviation is correct.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
  
  def validWordAbbriviation(self,word,abbr):
    
    word_pntr,abbr_pntr = 0,0
    
    while word_pntr < len(word) and abbr_pntr < len(abbr):
      
      if abbr[abbr_pntr].isdigit():
        
        step = 0
        
        if if abbr[abbr_pntr] == '0':
          return False
        
        while abbr_pntr < len(abbr) and abbr[abbr_pntr].isdigit():
          stap = step * 10 + int(abbr[abbr_pntr])
          abbr_pntr += 1
          
        word_pntr += step
      else:
        
        if abbr[abbr_pntr] != word[word_pntr]:
          return False
        
        abbr_pntr += 1
        word_pntr += 1
        
  return abbr_pntr == len(abbr) and word_pntr == len(word)
    
