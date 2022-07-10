def find_celebrity(n):

  matrix = [[0, 0, 1, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 0],
           [0, 0, 1, 0]]

  indegree = [0 for i in range(n)]
  outdegree = [0 for i in range(n)]

  for i in range(n):
    for j in range(n):

      x = matrix[i][j]
      print('value of x is',x)
      indegree[j] += x
      outdegree[i] += x

      print(indegree)
      print(outdegree)
  for i in range(n):

    if indegree[i] == n-1 and outdegree[i] == 0:
      return i

  return -1

def search_celebrity(n):

  candidate = 0
  for i in range(1,n):
    if knows(i,candidate) and not knows(candidate,i):
      continue
    else:
      candidate = i

  for j in range(candidate):
    if not knows(j,candidate) and not knows(candidate,j):
      return -1

  return candidate
    

def knows(i,j):
  matrix = [[0, 0, 1, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 0],
           [0, 0, 1, 0]]

  if matrix[i][j] == 1:
    return True
    
  return False
  
if __name__ == '__main__':
  n=4

  print(search_celebrity(n))
