# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# def listtolink(ls):
    
#     head=ListNode(0)
#     pre=head
    
#     for item in ls:
#         head.next=ListNode(item)
#         head=head.next
#     return pre.next

# def listNodeToString(node):
#     if not node:
#         return "[]"

#     result = ""
#     while node:
#         result += str(node.val) + ", "
#         node = node.next
#     return "[" + result[:-2] + "]"


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dia1=set() #(X+Y)右上左下的斜線"/"
        dia2=set() #(X-Y)左上右下的斜線"\"
        diax=set()

        res=0
        
        
        def nq(n,y):
            nonlocal res
            if y>=n:
                res+=1
                #print(ans)
                return
            
            
            for x in range(n):
                if x in diax or (x+y) in dia1 or (x-y) in dia2:
                    continue
                diax.add(x)
                dia1.add(x+y)
                dia2.add(x-y)
                nq(n,y+1)
            
                diax.remove(x)
                dia1.remove(x+y)
                dia2.remove(x-y)
            
            
        
        nq(n,0)
        
        return res
        

if  __name__ == "__main__":
    

    ret = Solution().totalNQueens(4)
    
    print(ret)
    

            