'''
'''

'''
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = {}
        
        for i,j in prerequisites:
            if j in adj_list:
                adj_list[j].append(i)
            else:
                adj_list[j] = [i]
        
        visited = [False]*numCourses
        result = []
        for i in range(numCourses):
            
            if not self.cycle(adj_list,visited,i,result):
                return []
            
        return result[::-1]
            
    
    def cycle(self,adj_list,visited,curnode,result):
        
        if visited[curnode] == -1:
            return False
        
        if visited[curnode] == 1:
            return True
        
        visited[curnode] = -1
        if curnode in adj_list:
            
            for i in adj_list[curnode]:
                if not self.cycle(adj_list,visited,i,result):
                    return False
        result.append(curnode)
        visited[curnode] = 1
        
        return True
