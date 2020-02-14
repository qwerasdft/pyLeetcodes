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
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        ans = [[0]*m for i in range(n)]

        for j in range(m):
            for i in range(n):
                if i == 0 or j == 0:
                    ans[i][j] = 1
                else:
                    ans[i][j] = ans[i-1][j]+ans[i][j-1]

        return ans[n-1][m-1]


if __name__ == "__main__":

    ret = Solution().uniquePaths(4, 3)

    print(ret)
