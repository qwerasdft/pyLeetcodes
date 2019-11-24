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





class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        

        def backtrack(n, k, res, temp, start):
            
            if k == 0:
                res.append(temp)
                return
            
            for i in range(start, n+1):
                backtrack(n, k-1, res, temp + [i], i+1)
                
        
        res = []
        backtrack(n, k, res, [], 1)
        
        return res

    def combine1(self, n, k):
        def backtrack(n, k,  temp, start):
            
            temp1=[]
            if k == 0:
                
                return  [temp]
            
            for i in range(start, n+1):
                temp1+=backtrack(n, k-1,  temp + [i], i+1)
            
            return temp1
        
        
        res =backtrack(n, k,  [], 1)
        
        return res


if  __name__ == "__main__":
    
    ret = Solution().combine1(4,3)
    
    print(ret)
