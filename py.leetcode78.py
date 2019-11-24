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
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #print('in=',nums)
        if nums == []: return [[]]
        mylist = [[nums[0]]]
        llist = self.subsets(nums[1:])
        mylist += llist
        mylist += [[nums[0]] + item for item in llist if item != []]
        #print('out=',mylist)
        return mylist
    
    def subsets1(self,nums):

        if nums==[] : return [[]]
        res=[]
        def help1(nums,start,temp,res):            
            res.append(temp)
            for i in range(start,len(nums)):
                help1(nums,i+1,temp+[nums[i]],res)

            
        
        help1(nums,0,[],res)
        return res
    
    # DFS recursively 
    def subsets2(self, nums):
        res = []
        self.dfs(nums, 0, [], res)
        return res
        
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)

        




    
if  __name__ == "__main__":
    a=[1,2,3]
    
    ret = Solution().subsets1(a)
    
    print(ret)
