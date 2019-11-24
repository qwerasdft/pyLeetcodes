
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
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        stacks=[]
        x=root
        if not x :
            return res
        
        
        while x or stacks:
            if x:
                res.append(x.val)
                stacks.append(x)
                x=x.left
            else:
                x=stacks.pop()
                x=x.right
                #if x:
                    #res.append(x.val)
        return res

    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        stacks=[]
        x=root
        if not x :
            return res
        
         
        while x or stacks:
            while x:
                res.append(x.val)
                stacks.append(x)
                x=x.left
            
            x=stacks.pop()
            x=x.right
                #if x:
                    #res.append(x.val)
        return res



if  __name__ == "__main__":
    a="[1,null,2,3]"

    al=stringToTreeNode(a)

    ret = Solution().preorderTraversal1(al)
    
    print(ret)
