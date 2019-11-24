# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# def listtolk(ls):
    
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
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #x=1534236469
        
        res1=str(x)
        if x < 0:
            res1=res1[1:]
            res1='-' + res1[::-1]
        else:
            res1=res1[::-1]
        
        res1 = int(res1)
        if (res1 > 2**31-1) or (res1 < -2**31):
            res1=0
        return res1

if  __name__ == "__main__":
    a=123453

    ret = Solution().reverse(a)
    
    print(ret)

            