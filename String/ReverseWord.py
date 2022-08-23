'''
# First split string and convert it to list.
# Now we have list of word.
# Run the reverse loop for each word and join one by one by space.

Time Complexity: O(n)
Space Complexity: O(1)
'''

'''
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Input: s = "the sky is blue"
Output: "blue is sky the"
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        
        k = s.split()
        return ' '.join(k[::-1])
