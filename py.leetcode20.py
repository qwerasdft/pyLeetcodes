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
    def isValid(self, s: 'str') -> 'bool':
        # ind={'(':')',')':'(','[':']',']':'[','{':'}','}':'{'}
        ind2 = {'(': -1, ')': 1, '[': -2, ']': 2, '{': -3, '}': 3}
        q = []
        for c in s:
            if ind2[c] > 0:
                if not q:
                    return False
                else:
                    a = q.pop()
                    if ind2[a]+ind2[c] != 0:
                        return False

            else:
                q.append(c)
        if len(q) != 0:
            return False

        return True


if __name__ == "__main__":
    a = "()[]{}"

    ret = Solution().isValid(a)

    print(ret)
