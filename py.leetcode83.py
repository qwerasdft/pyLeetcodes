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

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        start=head
        prehead=head

        if not head:
            return head
        
       

        while head:
            head=head.next
            while head and (head.val == prehead.val):
                head = head.next

            prehead.next=head
            prehead=prehead.next
            # head=head.next
        
        return  start
        

    
if  __name__ == "__main__":
    a=[1,1,2,2,2,2,3,4,5,5,5,5]

    al=listtolink(a)

    ret = Solution().deleteDuplicates(al)
    
    print(listNodeToString(ret))
