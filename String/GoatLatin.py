'''
# Run through loop of word in sentence.
# If first char of a word is vowel then append 'ma' and index+1 times 'a' end of that word.
# If first char is a constant then remove first char and append end of the word along with 'ma' and 'a' index+1 times.
# Iterate each words and follow same process.
# End of the loop return updated string.

Time Complexity: O(n)
Space Complexity: O(1)
'''

'''
You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.
We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
For example, the word "apple" becomes "applema".
If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.

Input: sentence = "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
'''

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        st = sentence.split()
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        
        for i in range(len(st)):
            
            if st[i][0] in vowel:
                st[i] = st[i]+'ma'+'a'*(i+1)
            
            else:
                st[i] = st[i][1:]+st[i][0]+'ma'+'a'*(i+1)
                
        return ' '.join(st)
