'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
'''

'''
'''

class Solution:
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        if endWord not in wordList:
            return []
        
        word_tree = self.getWordTree(beginWord, endWord, wordList)
        
        def dfs(node: str) -> List[List[str]]:
            if node == beginWord:
                return [[beginWord]]
            if node not in word_tree:
                return []

            res = []
            parents = word_tree[node]
            for parent in parents:
                res += dfs(parent)
            for r in res:
                r.append(node)
            return res

        return dfs(endWord)
    
    
    def getWordTree(self,
                    beginWord: str,
                    endWord: str,
                    wordList: List[str]) -> Dict[str, List[str]]:
        
        adjacency_list = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '.' + word[i+1:]
                adjacency_list[pattern].append(word)
        
        visited_tree = {beginWord: []}
        
        found = False
        
        q = deque([beginWord])
        while q and not found:
            n = len(q)
            
            visited_this_level = {}

            for i in range(n):
                word = q.popleft()
                
                for i in range(len(word)):
                    pattern = word[:i] + '.' + word[i+1:]

                    for next_word in adjacency_list[pattern]:
                        if next_word == endWord:
                            found = True
                            
                        if next_word not in visited_tree:
                            if next_word not in visited_this_level:
                                visited_this_level[next_word] = [word]
                                q.append(next_word)
                            else:
                                visited_this_level[next_word].append(word)
            
            visited_tree.update(visited_this_level)
            print(visited_tree)
        return visited_tree
