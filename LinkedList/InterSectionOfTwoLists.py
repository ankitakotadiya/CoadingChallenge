'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
'''

'''
# Traverse ListA and ListB parallely. 
# When one of the list reaches to it's end then assign head of the another list. 
# Let's say, If listB completed first so assign head of listA to listB. As we know listB has less nodes than lisA so once listA completes it's node meanwhile listB would have traversed that extra nodes in listA.
# Now listA reached to it's end assign head of listB to listA.
# Now both lists have equal number of nodes so we have to traverse until they intersect one point.

Time Complexity: O(m+n), m = length of larger list, n = number of nodes traverse to reach intersection.
Space Complexity: O(m+n1), length of lists. 

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        cur1 = headA
        cur2 = headB
        
        while cur1 != cur2:
            
            if cur1 is None:
                cur1 = headB
                
            else:
                cur1 = cur1.next
                
            if cur2 is None:
                cur2 = headA
                
            else:
                cur2 = cur2.next
                
        return cur1
