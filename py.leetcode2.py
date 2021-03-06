# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = tail = ListNode(0)
        s = 0
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            tail.next = ListNode(s % 10)
            tail = tail.next
            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


def listtolk(ls):

    head = ListNode(0)
    pre = head

    for item in ls:
        head.next = ListNode(item)
        head = head.next
    return pre.next


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


if __name__ == "__main__":
    a = [2, 4, 3]
    b = [5, 6, 4]
    # test = Solution()
    la = listtolk(a)
    lb = listtolk(b)
    ret = Solution().addTwoNumbers(la, lb)
    out = listNodeToString(ret)
    print(out)
