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
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        
        p=head
        ind=0
        
        
        while p:
            p=p.next
            ind+=1
        #print(ind)
        
        if n==ind:
            return head.next
        
        p=head
        ind2=0
        tmp=ListNode(0)
        while p:
            if ind2==ind-n-1:
                tmp=p
            # if ind2==ind-n+1:
                tmp.next=p.next.next
            p=p.next
            
            ind2+=1
        if n==1:
                tmp.next=None
        return head

if  __name__ == "__main__":
    a=listtolink([1,0,-1,0,-2,2])
    b=2
    
    test
    ret = Solution().removeNthFromEnd(a,b)
    out = listNodeToString(ret)
    
    print(out)

            