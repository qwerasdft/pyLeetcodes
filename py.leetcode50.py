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
    def myPow(self, a, b):
        if b == 0: return 1
        if b < 0: return 1.0 / self.myPow(a, -b)
        half = self.myPow(a, b // 2)
        if b % 2 == 0:
            return half * half
        else:
            return half * half * a

            # Leetcode中被人讨厌最多的题目之一。
            # 但其实是个很好的Recursion入门题目。

            # > Base Case:  b == 0
            # > Function: F(a ^ b) = F(a ^ b // 2) *  F(a ^ b // 2)
            # 不论我们返回时候如何，我们执行第一步，先设立Base Case:
            # if b == 0: return 1

            # 完了以后，我们要对大问题进行拆分，也就是不断的对b的值折半

            # 拆分：
            # half = self.myPow(a, b // 2)

            # 当拆分到了最小的问题，满足base case b == 0 的时候，我们则进行返回，返回时候有三种可能

            # Function的三种可能性：

            # 当b为偶数的时候，比如 2 ^ 100，拆分的时候就变成 (2 ^ 50) * (2 ^ 50)
            # 当b为基数的时候，比如 2 ^ 25，拆分的时候就变成 (2 ^12) * (2 ^ 12) * 2
            # 当b为负数的时候，返回 1.0 / self.myPow(a, -b)

if  __name__ == "__main__":
    a=[1,2,1,2]
    

    ret = Solution().myPow(2,4)
    
    print(ret)
    

            