'''
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
'''

'''
# We know that the ip address has 4 valid part and each part has max length 255 means 3 digit so will make max 3 combinations for each part.
# First we take first digit and make combination with after of it digits upto 4 parts.

Time Complexity: O(4*n*3)
Space Complexity: O(4*n)
'''

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        ans = []
        k = 0
        
        def backtrack(s,k, temp=''):
            if k==4 and len(s)==0:
                ans.append(temp[:-1])
                return
            if k==4 or len(s)==0:
                return

            for i in range(3):
                if k>4 or i+1>len(s):
                    break

                if int(s[:i+1])>255:
                    continue
                if i != 0 and s[0]=='0':
                    continue

                backtrack(s[i+1:], k+1, temp+s[:i+1]+'.')
                
        backtrack(s,k,'')
        return ans
