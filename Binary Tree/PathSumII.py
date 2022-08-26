'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
'''

'''
# Start traversing left and right sub tree recursively.
# In each call increase sum by current node value also store current node value in list.
# Once you reach leaf node check whether sum is equal to target sum or not if yes then store that our array which holds all the nodes from root to leaf into result.
# Once left and right subtree of any node is traversed pop that element root node from array to avoid invalid path.
# At the end return result.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def pathsumii(self,root,tsum,summ,result,patharr):
        
        if not root:
            return
        
        summ = summ + root.val
        patharr.append(root.val)
        
        if not root.left and not root.right:
            
            if summ == tsum:
                result.append(patharr.copy())
                
        else:
            self.pathsumii(root.left,tsum,summ,result,patharr)
            self.pathsumii(root.right,tsum,summ,result,patharr)
        
        patharr.pop()
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        result = []
        self.pathsumii(root,targetSum,0,result,[])
        
        return result
