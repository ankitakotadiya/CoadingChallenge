'''
Given an array of positive numbers, 
find the smallest positive integer value that cannot be represented as the sum of elements of any subset of a given set.
'''

'''
Input:  arr[] = {1, 1, 1, 1};
Output: 5

Input:  arr[] = {1, 1, 3, 4};
Output: 10
'''

'''
Time Complexity: O(N)
Space Complexity: O(1)
'''

def findsmallestint(arr,n):
  
  res = 1
  
  for val in arr:
    
    if val <= res:
      res = res + val
      
    else:
      break
      
  return res    
    
