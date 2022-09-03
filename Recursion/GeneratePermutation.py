'''
Write a program which takes as input an array of distinct integers and generates all permutations of that array. No permutation of the array may appear more than once.
'''

'''
# The idea is to generate all permutation that begin with A[0] and find possible permutation from A[1,n-1].
# Now will swap A[0] to A[1] and find all permutation A[1,n-1] and so on.

Time Complexity: O(n!)
Space Complexity:O(n)
'''

def permutations(A):
  
  def possible_permutations(i):
    
    if i == len(A) - 1:
      result.append(A.copy())
      return
    
    for j in range(i,len(A)):
      
      A[i],A[j] = A[j],A[i]
      
      possible_permutations(i+1)
      
      A[i],A[j] = A[j],A[i]
      
  result = []
  possible_permutations(0)
  return result
