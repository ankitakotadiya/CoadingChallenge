'''
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle. 0 - A gate. INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647. Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
'''

'''
# First will get the position of gates and append in visited to track so not visit it again also in queue.
# Now will use bfs to find minimum distance from gates to it's adjacent.
# So using BFS will pop one by one gate from que and mark it's adjacent as closer.

Time Complexity: O(m*n)
Space Complexity: O(k), k is number of gates and it's adjacent.
'''

def wals_gates(rooms):
  
  row = len(rooms)
  col = len(rows[0])
  visit = set()
  que = []
  
  def addrooms(r,c):
    
    if r < 0 or c < 0 or r == row or c == col or (r,c) in visit or rooms[r][c] == -1:
      return
    
    visit.add((r,c))
    que.append([r,c])
    
  for i in range(row):
    
    for j in range(col):
      
      if rooms[i][j] == 0:
        visit.add((i,j))
        que.append([i,j])
    
  dist = 0
  while que:
    
    for i in range(len(que)):
      
      r,c = que.pop(0)
      rooms[r][c] = dist
      addrooms(r-1,c)
      addrooms(r+1,c)
      addrooms(r,c-1)      
      addrooms(r,c+1)
      
    dist += 1
    
    
        
        
  
 
