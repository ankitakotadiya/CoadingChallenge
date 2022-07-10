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
