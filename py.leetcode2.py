# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = ListNode(0)
        res=p
        c=0
        while (l1 != None)or (l2 != None) :
            if l1 == None :
                l1= ListNode(0)
               
            if l2 == None :
                l2= ListNode(0)
                
                
            tmp=ListNode((l1.val+l2.val+c)%10)
            #print('aaa=',c)
            c=(l1.val+l2.val+c)//10
            #print('bbb=',c)
            l1=l1.next
            l2=l2.next
            p.next=tmp
            p=p.next
            #print('ccc=',c)
           
        #print('ddd=',c)
            
        if c != 0 :
            tmp = ListNode(c)
            
            p.next=tmp
            p=p.next
        
        return res.next
    
def listtolk(ls):
    
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

if  __name__ == "__main__":
    a=[2,4,3]
    b=[5,6,4]
    # test = Solution()
    la = listtolk(a)
    lb = listtolk(b)
    ret = Solution().addTwoNumbers(la,lb)
    out = listNodeToString(ret)
    print(out)

            