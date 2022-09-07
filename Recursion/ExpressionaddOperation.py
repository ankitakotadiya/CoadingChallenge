'''
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
'''

'''
Time Complexity: O(4^n)
Space Complexity: O(n)
'''

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        if not num: return []
        res = []

        def helper(start, expr, val, prev):
            if val == target and start == len(num):
                res.append(expr); return
            
            for i in range(start, len(num)):
                curr = num[start: i+1]
                if i > start and num[start] == '0': break   
                    
                if start == 0:
                    helper(i+1, curr, int(curr), int(curr))
                else:
                    helper(i+1, expr+'+'+curr, val+int(curr), int(curr))
                    helper(i+1, expr+'-'+curr, val-int(curr), -int(curr))   
                    helper(i+1, expr+'*'+curr, val-prev+prev*int(curr), prev*int(curr))   
        
        helper(0, '', 0, 0)
        return res
