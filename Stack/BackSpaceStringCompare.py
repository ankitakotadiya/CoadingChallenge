'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
'''

'''
# Run reverse loop of string1 and string 2 until length equal to the 0.
# If we encounter any char other than '#' then simply store at the top of the stack.
# If we encounter '#' then increase del count by one.
# In the next iteration current char is not '#' and del count greater than 0 so will not store current char into stack and will decrease del count by one.
# Will follow same process for the string 2 as well in the same iteration and store non deleted charactes at the top of the stack.
# At the end of iteration if we have both the stacks are equal then return True else False.

Time Complexity: O(max(n1,n2)), n1 and n2 are length of the string1 and string2
Space Complexity: O(n)
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        sr = len(s) - 1
        tr = len(t) - 1
        sdel = 0
        tdel = 0
        st1 = []
        st2 = []
        
        while sr >= 0 or tr >= 0:
            
            if sr >= 0:
                
                
                if s[sr] == '#':
                    sdel += 1
                    
                elif sdel > 0:
                    sdel -= 1
                    
                else:
                    st1.append(s[sr])
                    
                sr -= 1
                
            if tr >= 0:
                
                if t[tr] == '#':
                    tdel += 1
                    
                elif tdel > 0:
                    tdel -= 1
                    
                else:
                    st2.append(t[tr])
                    
                tr -= 1
                
        print('st1 st2',st1,st2)
        return st1 == st2
