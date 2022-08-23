'''
Given a string s which represents an expression, evaluate this expression and return its value. 

Input: s = "3+2*2"
Output: 7
'''

'''
# If the current character is dight in between 0-9 then add it to temporary variable called currentNumber.
# Otherwise current char must be an operation like (+,-,*,/). Evaluate an expression based on operation.
# If it is + or -, will evaluate expression later so push currentNumber in the stack to be later used. For addition push CurrentNumber and substraction push -currentNumber.
# For * and / pop value from the stack perfrom operation with currentNumber and popped valued from stack and push it back to the stack.
# Once string is scanned return sum of the all elements stored in the stack.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def calculate(self, s: str) -> int:
        
        operator = '+'
        operations = {'+','-','/','*'}
        cur = 0
        stack = []
        
        for c in range(len(s)):
            
            char = s[c]
            
            if char.isdigit():
                cur = cur * 10 + int(char)
            
            if char in operations or c == len(s) - 1:
                
                if operator == '+':
                    stack.append(cur)

                elif operator == '-':
                    stack.append(-cur)

                elif operator == '*':
                    stack.append(stack.pop()*cur)

                elif operator == '/':
                    q = int(stack.pop()/cur)
                    stack.append(q)
                    
                operator = char
                cur = 0
                
                
        return sum(stack)
