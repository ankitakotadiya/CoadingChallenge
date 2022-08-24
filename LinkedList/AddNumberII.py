'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
'''

'''
# Traverse list1 and convert nodes to number.
# Traverse list2 and convert nodes to numer.
# Add both the number so will get resultant number that we have to conver number to linked list nodes.
# Create one dummy which is head of new list.
# Create one temp and make reference to dummy.
# Convert above resultant node to string and iterate one by one char and set next node of temp and move temp to next.
# At the end return dummy's next Node.

Time Complexity: O(m+n+r) m,n,r length of list1,list2 and resultant list.
Space Complexity: O(r) r = length of resultant list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n1 = 0
        n2 = 0
        
        while l1 or l2:
            
            if l1:
                n1 = n1*10 + l1.val
                l1 = l1.next
                
            if l2:
                n2 = n2 * 10 + l2.val
                l2 = l2.next
                
        
        dummy = ListNode()
        poi = dummy
        
        for i in str(n1+n2):
            poi.next = ListNode(i)
            poi = poi.next
            
        return dummy.next
