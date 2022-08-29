'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
You can return the answer in any order.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
'''

'''
# First will use BFS to construct graph like dictionary means every node store as key and values are their neighbours.
# Then will use BFS to iterate k level starting from target node, so initially will push target node and it's distace to itself 0 in the stack.
# Will visit it's neighbour nodes and marked as visited simultaneiously increase depth plus 1 for it's neighbour.
# Once we get depth equal to target depth will store it's children in our result.
# If depth is greater than target then break the loop.
# At the end return result.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(list)
        stack = [root]
        
        while stack:
            
            node = stack.pop()
            
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                stack.append(node.left)
                
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                stack.append(node.right)
         
        q = []
        q.append((target.val,0))
        seen = set()
        seen.add(target.val)
        res = []
        
        while q:
            
            node,depth = q.pop(0)
            if k == depth:
                res.append(node)
                
            if depth > k:
                break
                
            for nei in graph[node]:
                
                if nei not in seen:
                    q.append((nei,depth+1))
                    seen.add(nei)
                    
        return res
