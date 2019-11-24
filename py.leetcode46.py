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



def insert_x(x, a):
    return [a[:i] + [x] + a[i:] for i in range(len(a) +1)] 
        
    
class Solution:
    """
    Given a collection of distinct integers, return all possible permutations.


    """
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return [nums]
        x = nums.pop()
        ways = self.permute(nums)
        res = []
        for w in ways:
            res += insert_x(x, w)
        return res



if  __name__ == "__main__":
    a=[1,2,3]
    

    ret = Solution().permute(a)
    
    print(ret)
    

            