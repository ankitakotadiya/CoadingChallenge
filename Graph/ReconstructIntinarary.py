'''
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
'''

'''
'''

class Solution:

  def reconstruct_intinarary(self,tickets):

    graph = {}

    for s,d in tickets:
      if s in graph:
        graph[s].append(d)
      else:
        graph[s] = [d]

    for src in graph.keys():
      graph[src].sort(reverse=True)

    stack = []
    res = []

    stack.append('JFK')

    while stack:

      ele = stack[-1]

      if ele in graph and len(graph[ele]) > 0:
        stack.append(graph[ele].pop())

      else:
        res.append(stack.pop())

    return res[::-1]
