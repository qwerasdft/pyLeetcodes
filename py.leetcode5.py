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
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        l = len(s)
        if s == None or l == 0:
            return ""
        nl = 2 * l + 1
        p = [0] * nl
        mx, pos = 0, 0
        for i in range(nl):
            if i > mx:
                p[i] = 1
            else:
                p[i] = min(p[2 * pos - i], mx - i)

            while i - p[i] >= 0 and i + p[i] < nl and self.get(s, i + p[i]) == self.get(s, i - p[i]):
                p[i] += 1

            if p[i] + i - 1 > mx:
                mx = p[i] + i - 1
                pos = i
        ml = ct = 0
        for i in range(nl):
            if p[i] > ml:
                ct = i
                ml = p[i]
        return s[((ct - ml + 1) // 2):((ct + ml) // 2)]

    def get(self, s, i):
        if i % 2 == 0:
            return "#"
        else:
            return s[i // 2]


if __name__ == "__main__":
    a = "babad"

    ret = Solution().longestPalindrome(a)

    print(ret)
