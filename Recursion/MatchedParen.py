'''
Write a program that takes as input a number and retums all the strings with that number of matched pairs of parens.
'''

'''
# Here will recursively add left and right paren.
# Initially assign n number of left and right paren.
# We can only open bracket or add left paren if number of left paren > 0 simultaneously decrease left paren by one.
# We can only close bracket if we have already open bracket that means left should be less than right.
# Once we reach to balance pair means left and right both 0 will append into our result.
# Otherwise, generate 2 pairs for each pair basis on condition matched.

Time Complexity: O(n*2^n)
Space Complexity: O(2*n)
'''

def generate_balance_paren(n):
  
  def directed_balanced_paren(left,right,bal_str,result=[]):

    if left > 0:
      directed_balanced_paren(left-1,right,bal_str+'(')

    if left < right:
      directed_balanced_paren(left,right-1,bal_str+')')

    if not right:
      result.append(bal_str)

    return result
    
  return directed_balanced_paren(n,n,'')

