'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

'''
# Create one dummy node which is head of the new linked list.
# Create one temporary head and make reference to dummy node.
# Traverse both the list until both reach to end.
# Initilise carry to 0.
# Calculate sum of the list1 value if present else 0 + list2 value if present else 0 and carry.
# Save carry  = 1 if sum > 9 else 0.
# Create a new node with last digit of the sum and set it to next of head.
# Move head to next.
# Move both the lists to next node.
# At the end of iteration if carry presents then append it to next node of head.
# Return dummy's next node.

Time Complexity: O(max(n1,n2)), n1 and n2 are number of node in both lists.
Space Complexity: O(max(n1,n2))
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        d = ListNode
        head = d
        c = 0
        
        while l1 or l2:
            
            a = 0 if not l1 else l1.val
            b = 0 if not l2 else l2.val
            
            n = a+b+c
            c = 1 if n > 9 else 0
            node = ListNode(n%10)
            
#             if not head:
#                 head = node
            
#             else :
#                 head.next = node
                
            head.next = node 
            head = head.next    
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
                
            if c:
                node = ListNode(1)
                head.next = node
             
            
            
        return d.next
