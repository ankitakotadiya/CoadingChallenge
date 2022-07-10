class Solution:
    def networkDelayTime(self, times, n, k):
      v = [float('inf') for i in range(n+1)]
      v[0] = float('-inf')
      print(v)

      adj = {}
      for s,d,t in times:
        if s not in adj:
          adj[s] = []
        adj[s].append([t,d])

      print(adj)

      def dfs(t,s):
        if s in adj:

          for dt,d in adj[s]:
            if v[d] > t+dt:
              v[d] = t+dt
              print(v[d])
              dfs(t+dt,d)

      v[k] = 0
      dfs(0,k)
      res = max(v)

      return -1 if res == float('inf') else res


obj = Solution()
print(obj.networkDelayTime([[1,2,1]],2,2))
