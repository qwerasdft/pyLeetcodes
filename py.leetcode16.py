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
    def threeSumClosest(self, nums: [int], target: int) -> int:
        self.tg=target
        self.nums=sorted(nums)
        self.lnum=len(nums)
        self.ans=float('inf')
        self.res=0
        #print(self.nums)
        
        for i in range(self.lnum-2):
            if i>0 and self.nums[i-1]==self.nums[i]:
                continue
            
            a=self.nums[i]
            
            j=i+1
            k=self.lnum-1
            while j<k:
                #print(a+nums1[j]+nums1[k])
                if abs(self.tg-a-self.nums[j]-self.nums[k])<self.ans:
                    self.ans=abs(self.tg-a-self.nums[j]-self.nums[k])
                    self.res=a+self.nums[j]+self.nums[k]
                
                
                if a+self.nums[j]+self.nums[k]<self.tg:
                    j+=1
                elif a+self.nums[j]+self.nums[k]==self.tg:
                    return a+self.nums[j]+self.nums[k]
                else:
                    k-=1
            
        return self.res
                
        

        
if  __name__ == "__main__":
    a=[-1,2,1,-4]
    b=1

    ret = Solution().threeSumClosest(a,b)
    
    print(ret)

            