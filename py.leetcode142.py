class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=fast=head
        
        ind=ListNode(0)
        
        while fast!=None and fast.next != None:
            slow=slow.next
            fast=fast.next.next
            ind.next=slow
            
            if slow == fast:
                ind=head
                while ind!=slow:
                    ind=ind.next
                    slow=slow.next
                
                return ind
        
        return None