
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stacks = []
        x = root

        if not x:
            return []

        while x or stacks:
            while x:
                stacks.append(x)
                x = x.left
            x = stacks.pop()
            res.append(x.val)
            x = x.right
        return res

    def inorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []

        def helper(aa):
            if not aa:
                return
            helper(aa.left)
            res.append(aa.val)
            helper(aa.right)

        helper(root)
        return res


if __name__ == "__main__":
    a = "[1,null,2,3]"

    al = stringToTreeNode(a)

    ret = Solution().inorderTraversal1(al)

    print(ret)
