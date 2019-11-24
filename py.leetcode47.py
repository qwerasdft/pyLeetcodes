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
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l)+1):
                    #插入新元素
                    new_ans.append(l[:i]+[n]+l[i:])
                    #插入在NEW_ANS[]第幾位後和原本的L[]比較 如果一樣就表示下一個插入會重複
                    if i<len(l) and l[i]==n: 
                        print("-----------")
                        break              #handles duplication
            #完成後取代原本得ans
            ans = new_ans
        return ans

if  __name__ == "__main__":
    a=[1,2,1,2]
    

    ret = Solution().permuteUnique(a)
    
    print(ret)
    

            