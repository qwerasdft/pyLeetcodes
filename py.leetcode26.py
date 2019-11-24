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
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        
        if len(nums)==0:
            return 0
        
        ind=1
        ans=[]
        ans.append(nums[0])
        for i in range(len(nums)):
            if i >0 and nums[i] != nums[i-1]:
                ind+=1
                ans.append(nums[i])
        nums[:]=ans
        return ind
                


if  __name__ == "__main__":
    a=[0,0,1,1,1,2,2,3,3,4]
    test

    ret = Solution().removeDuplicates(a)
    
    print(ret)
    print(a)

            