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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        start=head
        tmp=0
        
        
        
        while head:
            tmp+=1
            head=head.next


        if tmp == 0:
            return start    


        k=k%tmp

        if tmp == 1 or k==0:
            return start

        head=start

        for i in range(tmp):
            if i==tmp-1-k:
                tmp_h=head.next
                head.next=None
                break
            else:    
                head=head.next
        
        new_start=tmp_h

        while tmp_h:
            if tmp_h.next:
                tmp_h=tmp_h.next
            else :
                tmp_h.next=start
                break
        
    
        return new_start

if  __name__ == "__main__":
    
    a=[1,2,3]
    k=0


    ret = Solution().rotateRight(listtolink(a),k)
    
    print(listNodeToString(ret) )
    

            