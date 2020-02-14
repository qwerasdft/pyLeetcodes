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
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        digits[0] += 1

        for i in range(0, len(digits)):

            if digits[i]//10 > 0:

                digits[i] -= 10
                if i+1 == len(digits):
                    digits.append(1)
                else:
                    digits[i+1] += 1

        digits.reverse()
        return digits


if __name__ == "__main__":
    a = [1, 2, 3, 4]

    ret = Solution().plusOne(a)

    print(ret)
