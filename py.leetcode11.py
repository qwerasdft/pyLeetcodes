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
    def maxArea(self, height):
        length = len(height)

        start, end, mul = 0, length - 1, -1
        while start < end:

            mul = max(mul, min(height[start], height[end]) * (end - start))

            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return mul


if __name__ == "__main__":
    a = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    ret = Solution().maxArea(a)

    print(ret)
