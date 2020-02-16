class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def listtolink(ls):

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

# Given 1->2->3->4, you should return the list as 2->1->4->3.


class Solution:
    def swapPairs(self, head: "ListNode") -> "ListNode":
        dumH = ListNode(0)
        ind1 = ListNode(0)
        ind2 = ListNode(0)

        if not head or not head.next:
            return head

        dumH.next = head.next
        pre = head
        while pre:
            if pre and pre.next:
                ind1 = pre
                ind2 = pre.next
                tmpInd = ind2.next
                pre = pre.next.next

                ind2.next = ind1
                ind1.next = tmpInd.next if tmpInd else None

            else:
                ind1.next = pre
                return dumH.next
        return dumH.next


if __name__ == "__main__":
    a = listtolink([1, 2])

    ret = listNodeToString(Solution().swapPairs(a))

    print(ret)
