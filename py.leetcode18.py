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
    def fourSum(self, nums, target):
        nums.sort()
        ln = len(nums)
        double = {}
        results = []
        # 用于 储存两数相加的和值->两数可能的索引值的映射
        for a in range(ln):
            for b in range(a+1, ln):
                double.setdefault(nums[a] + nums[b], [])
                double[nums[a]+nums[b]] += [[a,b]]
                #print(double)
                # 复杂度是N(N-1)
        for c in range(ln-1):
            for d in range(c+1, ln-1):
                pos_inds = double.get(target - nums[c] - nums[d], [])
                # print(nums[c], nums[d], c, d)
                # print("// pos inds:", pos_inds)
                
                for a, b in pos_inds:
                    if a!= c and a!=d and b!=c and b!=d:
                        result = sorted([nums[c], nums[d], nums[a], nums[b]])
                        if result not in results:
                            results.append(result)

        return sorted(results)


if  __name__ == "__main__":
    a=[1,0,-1,0,-2,2]
    b=0
    

    ret = Solution().fourSum(a,b)
    
    print(ret)

            