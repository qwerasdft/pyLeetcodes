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
    """
    You are given a binary tree in which each node contains an integer value.

    Find the number of paths that sum to a given value.

    The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

    The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
    """

    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'int':
        self.ans = 0
        self.sums = {0: 1}

        self.df(root, 0, sum)
        return self.ans

    def df(self, root, cur, sum):
        if not root:
            return
        cur += root.val
        self.ans += self.sums.get(cur-sum, 0)
        self.sums[cur] = self.sums.get(cur, 0)+1
        self.df(root.left, cur, sum)
        self.df(root.right, cur, sum)
        self.sums[cur] = self.sums.get(cur, 0)-1


if __name__ == "__main__":

    root = stringToTreeNode("[10, 5, -3, 3, 2, null, 11, 3, -2, null, 1]")

    sums = 8
    Solution().pathSum(root, sums)
    print(Solution().pathSum(root, sums))
