'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Input: s = "(*))"
Output: true
'''

'''
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        leftmax = leftmin = 0
        
        for c in s:
            
            if c == '(':
                leftmax+=1
                leftmin+=1
                
            elif c == ')':
                leftmax-=1
                leftmin = max(0,leftmin-1)
                
            elif c == '*':
                leftmax += 1
                leftmin = max(0,leftmin-1)
                
            if leftmax < 0:
                return False
            
        if leftmin == 0:
            return True
