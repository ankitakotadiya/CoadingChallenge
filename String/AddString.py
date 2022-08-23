'''
# Run the reverse loop of both the strings.
# Add digits from both strings.
# If sum is greater than 9 then save carry = 1 else 0.
# Add last digit of sum to result string.
# Each and every iteration add sum to to the result and update carry.
# At the end of the loop if any carry the append resut string after carry.

Time Complexity: O(max(n1,n2)), n1 and n2 are length of the strings.
Space Complexity: O(1)
'''

'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Input: num1 = "11", num2 = "123"
Output: "134"
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        temp = carry = 0
        output = ''
        a = len(num1)-1
        b = len(num2) - 1
        
        while a>=0 or b>=0:
            
            i,j = 0,0
            
            if a>=0:
                i = int(num1[a])
                a-=1
                
            if b>=0:
                j = int(num2[b])
                b-=1
                
            temp = i+j+carry
            
            if temp > 9:
                carry = 1
            else:
                carry = 0
            output = str(temp)[-1]+output
            
        if carry:
            output = '1'+output
        
        return output
    
