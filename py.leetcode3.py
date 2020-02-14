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
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxN = tempN = 0
        l1 = []
        for i in range(len(s)):
            if s[i] not in l1:
                l1.append(s[i])
                tempN = len(l1)
                maxN = tempN if tempN > maxN else maxN
            else:
                l1 = l1[l1.index(s[i])+1:]
                l1.append(s[i])
        return maxN


if __name__ == "__main__":
    a = "abcabcbb"

    ret = Solution().lengthOfLongestSubstring(a)

    print(ret)
