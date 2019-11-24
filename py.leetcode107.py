
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
    
from collections import deque
class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        res=[]
        if not root:
            return res
        quroot = deque()
        quroot.append(root)
        
        
        while quroot:
            temp=[]
            tempq=[]
            while quroot:
                fistvalue=quroot.popleft()
                temp.append(fistvalue.val)
                if fistvalue.left:
                    tempq.append(fistvalue.left)
                if fistvalue.right:
                    tempq.append(fistvalue.right)
            res.append(temp)
            quroot.extend(tempq)
        
        return  res[::-1]

if  __name__ == "__main__":
    a="[3,9,20,null,null,15,7]"

    al=stringToTreeNode(a)

    ret = Solution().levelOrderBottom(al)
    
    print(ret)
