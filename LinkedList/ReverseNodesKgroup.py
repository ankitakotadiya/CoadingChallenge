'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
'''

'''
# First traverse k number of element and reverse them and assign it to res variable.
# Point head to the prevtail and update head = after k nodes.
# Now check if we have remaining nodes greater or equal to k then reverse them.
# Our prevtail contains head and first kth nodes already reversed so set prevtail's next node equal to current revresed node.
# Same as above update prevtail equal to head and head equal to remaining nodes.
# If number of nodes less than k then simply set prevtail's next node equal to remaining nodes.
# At the end return res.

Time Complexity: O(n)
SpaceComplexity: O(n)
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverser(node,k):
            
            prev = None
            cur = node
            
            while k:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                k-=1
                
            return prev
        
        # def helper(head, k):
        res = None
        curr = head
        prevtail = None
        while curr:
            count = 0
            while count < k and curr:
                curr = curr.next
                count += 1

            if count == k:
                revhead = reverser(head, k)
                if not res:
                    res = revhead
                

                if prevtail:
                    prevtail.next = revhead

                prevtail = head
                head = curr
        if prevtail:
            prevtail.next = head
        return res
