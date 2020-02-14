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


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0 for i in range(n+1)]

        # Top-Down
        # 这道题自顶向下的思考：如果要爬到n台阶，有两种可能性:

        # 在n-1的台阶处爬一层台阶
        # 在n-2的台阶处爬两层台阶
        # 继续向下延伸思考，到达每一次层一共有几种方法这个问题就变成了2个子问题：

        # 到达n-1层台阶有几种方法
        # 到达n-2层台阶有几种方法
        # 之后对返回子问题之和即可。
        def fs(nums):
            if nums <= 1:
                return 1
            if ans[nums] > 0:
                return ans[nums]
            ans[nums] = fs(nums-1)+fs(nums-2)
            return ans[nums]

        return fs(n)

        # Bottom-Up (Constant Space)
    def climbStairs1(self, n):
        if n == 1:
            return 1
        a, b = 1, 2
        for _ in range(2, n):
            a, b = b, a + b
        return b


if __name__ == "__main__":

    ret = Solution().climbStairs1(2)

    print(ret)
