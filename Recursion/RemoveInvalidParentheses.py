'''
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Input: s = "()())()"
Output: ["(())()","()()()"]
'''

'''
Time Complexity: O(2^n)
Space Complexity: O(n)
'''

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        l , r = 0,0
        ans = []
        
        for c in s:
            
            if c == '(':
                l+=1
                
            elif c == ')':
                
                if l > 0:
                    l -= 1
                    
                else:
                    
                    r += 1
                    
                    
        def isvalid(s):
            
            count = 0
            for c in s:
                
                if c == '(': count += 1
                    
                if c == ')': count -= 1
                    
                if count < 0:
                    return False
                
            return count == 0
        
        def backtrack(comb,start,left,right):
            
            cur_str = ''.join(comb)
            
            if left == 0 and right == 0 and isvalid(cur_str):
                ans.append(cur_str)
                return
            
            for i in range(start,len(s)):
                
                if s[i] != '(' and s[i] != ')':
                    continue
                    
                if i != start and s[i] == s[i-1]:
                    continue
                    
                if left > 0 and s[i] == '(':
                    comb[i] = ''
                    backtrack(comb,i+1,left-1,right)
                    comb[i] = s[i]
                    
                elif right > 0 and s[i] == ')':
                    comb[i] = ''
                    backtrack(comb,i+1,left,right-1)
                    comb[i] = s[i]
                    
        backtrack(list(s),0,l,r)
        return ans
