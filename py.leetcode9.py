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
    def isPalindrome(self, x: 'int') -> 'bool':
        if x < 0:
            return False
        x = str(x)
        wx = len(x)

        for i in range(wx//2):
            if x[i] != x[wx-1-i]:
                return False
        return True


if __name__ == "__main__":
    a = 123453

    ret = Solution().isPalindrome(a)

    print(ret)
