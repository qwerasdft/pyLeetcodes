
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return ans

        def help(root, level):
            nonlocal ans
            if root.left:
                ans = max(ans, help(root.left, level+1))
            if root.right:
                ans = max(ans, help(root.right, level+1))
            return max(ans, level)

        ans = help(root, 1)

        return ans


if __name__ == "__main__":
    a = "[3,9,20,null,null,15,7]"

    al = stringToTreeNode(a)

    ret = Solution().maxDepth(al)

    print(ret)
