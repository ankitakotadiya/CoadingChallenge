'''
# Run the loop of string from 1 to length of the string.
# Check current character is equal to previous one then increase count for that char.
# When char doesn't match with previous one then append previous character along with it's count if greater than 1 to the compress string.
# Follow above steps until you reached end of the string.
# Convert string to list and return result.

Time Complexity: O(n)
Space Complexity: O(n)
'''

'''
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
'''

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        r = ""
        l = len(chars)

        if l == 0:
            return ""

        if l == 1:
            return len(chars)

        cnt = 1
        i = 1
    
        while i < l:

            if chars[i] == chars[i - 1]: 
                cnt += 1
            else:
                r = r + chars[i - 1] if cnt == 1 else r + chars[i - 1] + str(cnt)
                cnt = 1

            i += 1
        
        r = r + chars[i - 1] if cnt == 1 else r + chars[i - 1] + str(cnt)
        
        chars[:] = list(r) 

        return len(chars)
