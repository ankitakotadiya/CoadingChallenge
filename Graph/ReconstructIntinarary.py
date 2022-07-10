class Solution:

  def reconstruct_intinarary(self,tickets):

    graph = {}
    for s, d in tickets:
      if d not in graph:
          graph[d] = []
      if s in graph:
          graph[s].append(d)
          graph[s].sort()
          continue
      graph[s] = [d]

    print(graph)
    def findPath(source, graph, visited, totalLen):
      if len(visited) == totalLen:
          return True, [source]
      choices = graph[source]
      for i in choices:
          if visited.count((source, i)) == choices.count(i):
              continue
          visited.append((source, i))
          flag, li = findPath(i, graph, visited, totalLen)
          print(li)
          if flag:
              return True, [source] + li
          visited.pop()
      return False, []
    flag, itinerary = findPath("JFK", graph, [], len(tickets))
    return itinerary

obj = Solution()
print(obj.reconstruct_intinarary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
