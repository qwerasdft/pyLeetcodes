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
    def threeSum(self, nums):
        ans=[]
        n=len(nums)
        nums.sort()
        
        
        for j in range(n-2):
            if j>0 and nums[j]==nums[j-1]:
                continue
                    
            newt=-nums[j]
            dic={}
                
            for k in range(j+1,n):
                    #if k >j+1 and nums[k]==nums[k-1]:
                        #print("pass",k)
                        #continue
                gap = newt-nums[k]
                    #print(i,j,k,gap)
                if gap in dic:
                    if [nums[j],nums[k],dic[gap]] in ans:
                        continue
                    ans.append([nums[j],nums[k],dic[gap]])
                dic[nums[k]]=nums[k]
        
        return ans


        
if  __name__ == "__main__":
    a=[-1,0,1,2,-1,-4]

    ret = Solution().threeSum(a)
    
    print(ret)

            