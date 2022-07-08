class Solution:
  
  def canFinish(self, numCourses, prerequisites):
    if len(prerequisites) == 0:
       return True
    visited = [0 for i in range(numCourses)]
    
    adj_list = self.make_graph(prerequisites)
    print(adj_list)
    
    for i in range(numCourses):
       if not visited[i]:
          if not self.cycle(adj_list,visited,i):
             return False
    return True
      
  def cycle(self,adj_list,visited,current_node):
    
    if visited[current_node] ==-1:
       return False
    if visited[current_node] == 1:
       return True
    visited[current_node] = -1
    if(current_node in adj_list):
       for i in adj_list[current_node]:
          if not self.cycle(adj_list,visited,i):
             return False
    visited[current_node] = 1
    
    return True
     
  def make_graph(self,array):
    adj_list = {}
    for i,j in array:
       if j in adj_list:
          adj_list[j].append(i)
       else:
          adj_list[j] = [i]
    return adj_list


obj = Solution()
print(obj.canFinish(3,[[0,1],[0,2],[1,2]]))
