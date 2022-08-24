'''
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:
'''

'''
# Take one cur pointer which will point to our head.
# Start from the head and move one step each time to the next node.
# When cur node meet with child, follow it's child chain to the end and connect end of child to the cur node's next node.
# Also connect cur node with start of child node.
# Move cur node by one to next node follow above steps if find any child else return head of the list.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        cur = head
        
        while cur:
            
            if cur.child:
                child = cur.child
                
                while child.next:
                    child = child.next
                    
                child.next = cur.next
                
                if cur.next:
                    cur.next.prev = child
                    
                cur.next = cur.child
                cur.next.prev = cur
                cur.child = None
                
            cur = cur.next
            
        return head
