'''
Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into the list such that it remains a cyclic sorted list. The given node can be a reference to_any_single node in the list, and may not be necessarily the smallest value in the cyclic list.

'''

'''
# Create a new node using given value.
# If head is None then return new created node.
# Set prev and cur value as head and head's next node.
# Iterate one by one node and check whether new node falls in between prev and cur. If yes then break loop and set prev's next node new node and new node's next cur.
# If move prev and cur node pointer.
# If prev node is greater than prev in such case will check if new node is less than or equal cur node then will break loop and set prev's next new node and new node's next cur.
# If not then agian move prev and cur pointer.
# After moving check if prev = head then we already completed cycle break loop from there.

Time Complexity: O(n)
Space Complexity: O(n)
'''
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
        
class Solution:
  
  def insert(self,head,val):
    
    node = Node(val,head)
    if not head:
      return node
    
    prev,cur = head,head.next
    while True:
      
      if prev.val <= val <= cur.val:
        break
        
      elif prev.val > cur.val and (val <= cur.val or val >= prev.val):
        break
        
      prev,cur = prev.next,cur.next
      
      if prev == head:
        break
        
    prev.next = node
    node.next = cur
    
    return head
      
