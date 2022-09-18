'''
In a party of N people, only one person is known to everyone. Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party. We can only ask questions like “does A know B? “. Find the stranger (celebrity) in the minimum number of questions.

Input Matrix:

matrix = [[0, 0, 1, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 0],
           [0, 0, 1, 0]]
'''

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
    
def find_celebrity(n,matrix):

  stack = []

  for i in range(n):
    stack.append(i)

  while len(stack) > 1:

    A = stack.pop()
    B = stack.pop()

    if matrix[A][B]:
      stack.append(B)

    else:
      stack.append(A)

  cele = stack.pop()

  for i in range(n):

    if i != cele:

      if matrix[i][cele] == 0 or matrix[cele][i] == 1:
        return -1

  return cele


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
