'''
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".

Input: s = "((("
Output: 3
'''

'''
# We keep track of balance string. For example, count of '('(opening bracket) - count of ')'(closing bracket).
# Iterate one by one bracket and update balance_bracket_count. If it is negative then need to add bracket to make it balanced so will increase valid_count by one and set back balance_bracket_count to 0.
# So, after this bracket we can easily track balanced bracket count.
# At the end of iteration return valid_count + balance_bracket_count which would be our answer.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack, moves = 0, 0
        for p in range(len(s)):
            if s[p] == "(":
                stack += 1
            else:
                stack -= 1
            
            if stack < 0:
                moves += 1
                stack = 0 
                
            # p += 1
                
        return moves + stack
