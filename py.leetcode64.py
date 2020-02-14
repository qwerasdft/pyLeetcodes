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
    def minPathSum(self, grid: 'List[List[int]]') -> 'int':
        minans = float('inf')

        h = len(grid)
        w = len(grid[0])
        for i in range(h):
            for j in range(w):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])

        return grid[h-1][w-1]


if __name__ == "__main__":
    a = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

    ret = Solution().minPathSum(a)

    print(ret)
