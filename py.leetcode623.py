class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


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
    Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v 
    at the given depth d. The root node is at depth 1.

    The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, 
    create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left 
    subtree should be the left subtree of the new left subtree root, its original right subtree should be 
    the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, 
    then create a tree node with value v as the new root of the whole original tree, and the original tree is 
    the new root's left subtree.
    """

    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        tmp = root
        if not root:
            return None
        if d == 1:
            tmp1 = TreeNode(v)
            tmp1.left = root
            return tmp1

        def rs(tmp, v, d, ind):
            if ind == (d-1):
                nl = tmp.left
                nr = tmp.right
                # print("=====a",oldNd,tmp)

                tmp.left = TreeNode(v)
                tmp.left.left = nl
                tmp.right = TreeNode(v)
                tmp.right.right = nr
                return

            else:
                # print("====b",tmp.val)
                if tmp.left:
                    rs(tmp.left, v, d, ind+1)
                if tmp.right:
                    rs(tmp.right, v, d, ind+1)

        rs(tmp, v, d, 1)

        return root


if __name__ == "__main__":

    root = stringToTreeNode("[4,2,6,3,1,5]")

    v = 1
    d = 2

    print(treeNodeToString(Solution().addOneRow(root, v, d)))
