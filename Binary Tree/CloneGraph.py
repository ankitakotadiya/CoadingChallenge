class Node:

  def __init__(self,val,neighbors=None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

class Solution:
    
    def cloneGraph(self,node):

      oldtonew = {}

      def dfs(node):
        if node is None:
          return None

        if node.val in oldtonew:
          return oldtonew[node.val]

        copy = Node(node.val)
        oldtonew[node.val] = copy

        for nei in node.neighbors:
          copy.neighbors.append(dfs(nei))
          # print(copy.val)

        return copy

      return dfs(node)
  
  
# if __name__ == '__main__':

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2,node4]
node2.neighbors = [node1,node3]
node3.neighbors = [node2,node4]
node4.neighbors = [node1,node3]

obj = Solution()
print(obj.cloneGraph(node1))
