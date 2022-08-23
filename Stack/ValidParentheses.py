'''
# First handle the case like if length of the string is odd that means brackets are not balanced so return False.
# The idea is to iterate one by one brackets and store opening brackets to stack.
# When current char is closing bracket, search in the stack, if holds same nature of opening bracket then pop and continue iteration.
# At the end if stack is empty that means all brackets are balanced return True else False.

Time Complexity: O(n)
Space Complexity: O(n)
'''

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()[]{}"
Output: true
'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        hm = {')':'(',
             '}':'{',
             ']':'['}
        
        if len(s) % 2 != 0:
            return False
        
        for i in s:
            
            if i in ['(','{','[']:
                stack.append(i)
                
            elif i in [')','}',']'] and stack:
                
                if hm[i] != stack.pop():
                    return False
            elif i in [')','}',']']:
                return False
                
        return len(stack) == 0
