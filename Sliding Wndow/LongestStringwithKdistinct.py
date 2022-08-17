class Solution:
  def longest_string_kth_distinct_character(self,s,k):

  start = 0
  longest = 0
  map = {}

  for end in range(len(s)):

    if s[end] in map.keys() :
      map[s[end]] += 1
        
    else:
      map[s[end]] = 1

    while len(map) > k:
      
      if map[s[start]] == 1:
        del map[s[start]]
      else:
        map[s[start]] -= 1
        
      start += 1

    longest = max(longest,end-start+1)

  return longest

obj = Solution()
print(obj.longest_string_kth_distinct_character('ababcbcca',2))
