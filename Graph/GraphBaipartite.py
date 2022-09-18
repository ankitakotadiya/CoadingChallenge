class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        colors = [None]*len(graph)
        que = []
        
        for i in range(len(graph)):
            
            if colors[i] is None:
                
                colors[i] = 1
                
                que = [i]
                
                while que:
                    cur_node = que.pop(0)
                    
                    for node in graph[cur_node]:
                        
                        if colors[node] is None:
                            colors[node] = 1 - colors[cur_node]
                            que.append(node)
                            
                        elif colors[node] == colors[cur_node]:
                            return False
                        
            return True

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        self.graph = graph
        self.visited = [False] * n
        self.color = {}
        self.ans = True

        for i in range(n):

          if not self.visited[i]:
            self.dfs(i,True)

        return self.ans
    
    def dfs(self,i,iscolored):

        self.visited[i] = True
        self.color[i] = iscolored

        for j in self.graph[i]:

          if not self.visited[j]:

            self.dfs(j,not iscolored)
            if self.ans == False:
              return
          else:

            if self.color[i] == self.color[j]:
              self.ans = False
              return
