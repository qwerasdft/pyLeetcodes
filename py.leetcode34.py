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
    """
    Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
    """

    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        if len(nums) == 0:
            return [-1, -1]

        self.nums = [float('-inf')]+nums+[float('inf')]
        self.target = target
        l = self.fl(0, len(self.nums)-1, target)
        h = self.fh(0, len(self.nums)-1, target)

        return [-1, -1] if l == -1 else [l-1, h-1]

    def fl(self, l, h, tg):
        if l+1 == h:
            if self.nums[h] == tg:
                return h
            else:
                return -1

        if l <= h:
            m = (l+h)//2

            if self.nums[m] < tg:
                # print("LLL",l,h,"nums=",self.nums[m])
                return self.fl(m, h, tg)
            else:
                # print("HHH",l,h,"nums=",self.nums[m])
                return self.fl(l, m, tg)  # 3,5

    def fh(self, l, h, tg):

        if l+1 == h:
            if self.nums[l] == tg:
                return l
            else:
                return -1

        if l <= h:
            m = (l+h)//2

            if self.nums[m] > tg:
                # print("LLL",l,h,m,"nums=",self.nums[m])
                return self.fh(l, m, tg)
            else:
                # print("HHH",l,h,m,"nums=",self.nums[m])
                return self.fh(m, h, tg)


if __name__ == "__main__":
    a = [5, 7, 7, 7, 7, 8, 8, 8, 8, 10]
    b = 8

    ret = Solution().searchRange(a, b)

    print(ret)
