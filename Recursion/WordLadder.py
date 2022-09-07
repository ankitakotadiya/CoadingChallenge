'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
'''

'''
'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        L = len(beginWord)
        dic = defaultdict(list)
        for word in wordList:
            
            for i in range(L):
                
                dic[word[:i]+'*'+word[i+1:]].append(word)
                
                
        que = deque([(beginWord,1)])
        visited = set()
        visited.add(beginWord)
        
        print(dic)
        while que:
            
            cur_word,level = que.popleft()
            
            for i in range(L):
                inter_word = cur_word[:i]+'*'+cur_word[i+1:]
                
                for word in dic[inter_word]:
                    
                    if word == endWord:
                        return level + 1
                    
                    if word not in visited:
                        visited.add(word)
                        que.append((word,level+1))
                        
        return 0
