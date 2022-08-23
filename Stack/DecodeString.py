'''
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4]

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
'''

'''
# Loop through character of string. Also intitilise stack along with empty string.
# If current char is num then first will convert it to int and store into temp variable.
# Once we see char is equal to '[' will push number at top of the stack.
# If we find current element is alpha then store append top of the stack.
# In case next element again alpha then append it with previously stored char and keep at top of the stack. Follow same process for all the consecutive alpha.
# Once we reach at closing bracket ']' will pop previously store characters and pop number multiply it with characters and store append it with last element.
# Follow same process to the end of the string.
# At the end return all joined element in stack.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = ['']
        num = 0
        
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append(num)
                num = 0
                stack.append("")
            elif ch == ']':
                _str = stack.pop()
                repeat_count = stack.pop()
                stack[-1] += _str * repeat_count
            else:
                stack[-1] += ch
        
        return ''.join(stack)

