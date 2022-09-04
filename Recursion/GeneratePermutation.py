'''
Write a program which takes as input an array of distinct integers and generates all permutations of that array. No permutation of the array may appear more than once.
'''

'''
# The idea is to generate all permutation that begin with A[0] and find possible permutation from A[1,n-1].
# Now will swap A[0] to A[1] and find all permutation A[1,n-1] and so on.

Time Complexity: O(n*n!)
Space Complexity:O(n)
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def possible_permutations(i,result=[]):
    
            if i == len(nums) - 1:
                result.append(nums.copy())
                
            
            for j in range(i,len(nums)):
                nums[i],nums[j] = nums[j],nums[i]
                
                possible_permutations(i+1)
                
                nums[i],nums[j] = nums[j],nums[i]
                
            return result
                
        return possible_permutations(0)
