'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''

'''
# Create one initial index and initilise to 0.
# Create one hashmap which store key as number and value as alpha.
# Run through loop of first digit's value lets say number is 23 so first will get string 'abc'.
# Recursively will make possible pairs with 3 which value is 'def'. Once get formed path equal to length of digits will append path to our result.

Time Complexity: O(4^n), maximum length of alpha.
Space Complexity: O(4^n)
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        result = []
        
        if len(digits) == 0:
            return result
        
        def dfs(indx,path):
            
            if indx >= len(digits):
                result.append(path)
                return
            
            str1 = dic[digits[indx]]
            
            for i in str1:
                dfs(indx+1,path+i)
                
        dfs(0,'')
        return result
