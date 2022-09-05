'''
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Input: n = 2
Output: ["11","69","88","96"]
'''

'''
# Create a one dictionary which stores number and it's strobogrametic correspond value.
# Run through loop for each key value in dict.
# Start pointer will set to 0 and end pointer n-1. At t time we generate 2 combination so will make recursion call n/2.
# Once start > end will store stobo num in our result.
# For each key in dict we generate possible strobo num.

# Time Complexity: O(5^(n/2))
# Space Complexity: O(5^(n/2))
'''

def findStrobogrammatic(n):

  result = [None]*n
  output = []
  stro_dict = {'0':'0','1':'1','6':'9','9':'6','8':'8'}
  def dfs(start,end,result):

    if start > end:
      output.append(''.join(result))
      return

    for num in stro_dict:

      if start != end and num == '0' and start == 0:
        continue

      if start == end and num in ('6','9'):
        continue

      result[start],result[end] = num,stro_dict[num]

      dfs(start+1,end-1,result)

  dfs(0,n-1,result)
  return output
