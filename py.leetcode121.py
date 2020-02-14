
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# def stringToTreeNode(input):
#     input = input.strip()
#     input = input[1:-1]
#     if not input:
#         return None

#     inputValues = [s.strip() for s in input.split(',')]
#     root = TreeNode(int(inputValues[0]))
#     nodeQueue = [root]
#     front = 0
#     index = 1
#     while index < len(inputValues):
#         node = nodeQueue[front]
#         front = front + 1

#         item = inputValues[index]
#         index = index + 1
#         if item != "null":
#             leftNumber = int(item)
#             node.left = TreeNode(leftNumber)
#             nodeQueue.append(node.left)

#         if index >= len(inputValues):
#             break

#         item = inputValues[index]
#         index = index + 1
#         if item != "null":
#             rightNumber = int(item)
#             node.right = TreeNode(rightNumber)
#             nodeQueue.append(node.right)
#     return root

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = float("inf")
        maxprofit = 0

        for i in prices:
            minprice = min(minprice, i)
            maxprofit = max(maxprofit, i-minprice)

        return maxprofit


if __name__ == "__main__":
    a = [7, 1, 5, 3, 6, 4]

    ret = Solution().maxProfit(a)

    print(ret)
