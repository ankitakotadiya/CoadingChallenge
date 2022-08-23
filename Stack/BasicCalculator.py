'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''

'''
# Intially set curNumber,output,sign,stack = 0,0,1,[].
# Calculate number one by one and add it output += curNumber * sign. Update sign and curNumber in each iteration.
# When we see '(' push intermediate result calculation in the stack also push sign(either 1 or -1) at the top of the stack and start new calculation right after '('.
# When we see ')' pop 1/-1 as sign from the stack multiply with output also pop previous calculation and add it with output.
# Follow the same step until scan is done.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def calculate(self, s: str) -> int:
        
        cur,output,sign,stack = 0,0,1,[]
        
        for ch in s:
            
            if ch.isdigit():
                cur = cur*10 + int(ch)
                
            elif ch == '+':
                output += sign*cur
                sign = 1
                cur = 0
                
            elif ch == '-':
                output += sign*cur
                sign = -1
                cur = 0
                
            elif ch == '(':
                stack.append(output)
                stack.append(sign)
                sign = 1
                output = 0
                
            elif ch == ')':
                output += sign*cur
                output *= stack.pop()
                output += stack.pop()
                cur = 0
                
        return output + sign * cur

