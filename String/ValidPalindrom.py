'''
# It first converts all the character in a sentence to lowercase.
# Now run the loop 0 to length of the sentence and remove character if it is not alpha numeric.
# If sentence and it's reverse is same then will return the result True else False.

Time Complexity: O(n)
Space Complexity: O(1)
'''

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        
        for e in s:
            
            if not e.isalnum():
                s = s.replace(e,"")
                
        return s == s[::-1]
