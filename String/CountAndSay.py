'''
# The idea is to generate all terms from 1 to n. First two term initilise as '1' and '11' and all another term generate from previous term.
# Run the loop from start 3 to n+1 because two terms are fixed. While scanning a term simply keep track of count of all consecutive characters.
# For a sequence of the same character, we append the count followed by a character to generate next term.

Time Complexity: O(n*l), n is the length of term and l is the length of string for each term.
Space Complexity: O(1)
'''

'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
'''

class Solution:
    def countAndSay(self, n: int) -> str:
        
        if (n == 1):
            return "1"
        if (n == 2):
            return "11"

        s = "11"
        for i in range(3, n + 1):

            s += '$'
            l = len(s)

            cnt = 1 
            tmp = "" 

            for j in range(1 , l):

                if (s[j] != s[j - 1]):

                    tmp += str(cnt + 0)
                    tmp += s[j - 1]
                    cnt = 1

                else:
                    cnt += 1

            s = tmp
        return s
