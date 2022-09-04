'''
Write a program which computes all size k subsets of 11,,2,...,?tl, where k and n are Pto- gram inputs. For example, iI k = 2 and n = 5, then the result is the following:
{{1, 2}, {1, 3}, {1, 4}, {1, 5}, [2, 3}, {2, 4}, {2, 5}, {3, 4}, {3, 5}, {4, 5}}
'''

'''
# Simple approach is first we check does it contain 1 or not.
# If not then first compute k size subset of [2...n] if contain 1 then we compute k-1 size subset of 2 to n and simply add 1 to each of them.
# Final answer will get if I take as an example 1,2,3 then {2,3},{1,3},{1,2}

Time Complexity: n*(n^k)
Space Complexity: O(n)
'''

def generate_power_set_k(n,k):
  
  def directed_power_set(offset,combination):
    
    if len(combination) == k:
      result.append(list(combination))
      return
    
    num_remaining = k - len(combination)
    i = offset
    while i <= n and num_remaining <= n - i + 1:
      directed_power_set(i+1,combination + [i])
      i+=1
    
  result = []
  directed_power_set(1,[])
  return result
