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
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        k = False
        for a in matrix:
            k = k or target in a
        
        return(k)


if  __name__ == "__main__":
    a=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]

    ret = Solution().searchMatrix(a,3)
    
    print(ret)

    # arr=[[0]*6 for i in range(4)]
    # for i in range(6*4):
    #     a=i//6
    #     b=i%6
    #     arr[a][b]=(a,b)
    

            