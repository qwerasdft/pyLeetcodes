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
    def letterCombinations(self, digits: str) -> [str]:
        if digits == "":
            return []

        pd = {'2': ['a', 'b', 'c'],
              '3': ['d', 'e', 'f'],
              '4': ['g', 'h', 'i'],
              '5': ['j', 'k', 'l'],
              '6': ['m', 'n', 'o'],
              '7': ['p', 'q', 'r', 's'],
              '8': ['t', 'u', 'v'],
              '9': ['w', 'x', 'y', 'z'],
              '1': ['*'],
              '0': [' ']}

        ans = []
        # for num1 in pd[1]:
        #    for num2 in pd[0]
        #        ans += num1+num2

        que = []
        for num in digits:
            que.append(pd[num])

        # def help(que,qind,qend,tmp):
        #     if qind==qend:
        #         ans.append(tmp)
        #         return
        #     for inq in que[qind]:
        #         help(que,qind+1,qend,tmp+inq)

        def help(que, qini, qend, tmp):
            if qini == qend:
                ans.append(tmp)
                return
            else:
                for wd in que[qini]:
                    help(que, qini+1, qend, tmp+wd)

        help(que, 0, len(digits), '')
        return ans


if __name__ == "__main__":
    a = "23"

    ret = Solution().letterCombinations(a)

    print(ret)
