
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def listtolink(ls):
    
    head=ListNode(0)
    pre=head
    
    for item in ls:
        head.next=ListNode(item)
        head=head.next
    return pre.next

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=fast=head
        
        while fast != None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            
            if slow == fast:
                return True
        
        return False                    
                    
        
if  __name__ == "__main__":
    a=[3,2,0,-4]
    a=listtolink(a)
    Solution().hasCycle(a)
    
    print(a)
