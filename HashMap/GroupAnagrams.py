'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

'''
# Run through loop of each word.
# Each and every iteration sort word and keep adding word in the hashmap against sorted key.
# At the end of the loop return values of hashmap which would be our answer.

Time Complexity: O(n * nlogn)
Space Complexity: O(1)
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        for word in strs:
            
            sortedword = ''.join(sorted(word))
            
            if sortedword in dic:
                dic[sortedword].append(word)
            
            else:
                dic[sortedword] = [word]
                
        return dic.values()
            
