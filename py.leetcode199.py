
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
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Input: [1,2,3,null,5,null,4]
        Output: [1, 3, 4]
          1            <---
        /      
       2     3         <---

         5     4       <---
        """
        if not root:
            return []

        def helper(r, lev):
            if len(res) < lev:

                res.append(r.val)

            if r.right:
                helper(r.right, lev+1)
            if r.left:
                helper(r.left, lev+1)

        res = []

        helper(root, 1)

        return res
        # return [res[x][-1] for x in range(len(res))]


if __name__ == "__main__":
    a = "[1,2,3,null,5,null,4]"

    al = stringToTreeNode(a)

    ret = Solution().rightSideView(al)

    print(ret)
