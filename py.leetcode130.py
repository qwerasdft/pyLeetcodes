
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
    def solve(self, grid):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if grid ==[]:
            return 
        
        r= len(grid)
        c= len(grid[0])
        

        def helper(i,j):
            if i>=0 and i < r and j >=0 and j < c and grid[i][j]== 'O':
                grid[i][j]='#'
                helper(i+1,j)
                helper(i-1,j)
                helper(i,j+1)
                helper(i,j-1)
            else:
                return
        
        for i in range(r):
            helper(i,0)
            helper(i,c-1)
            
        for j in range(c):
            helper(0,j)
            helper(r-1,j)
        
        for i in range(r):
            for j in range(c):
                #print(i,j,grid[i][j])
                if grid[i][j] == '#':
                    grid[i][j] = 'O'
                else:
                    grid[i][j] = 'X'
                    
                    
        
if  __name__ == "__main__":
    a=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
   

    Solution().solve(a)
    
    print(a)
