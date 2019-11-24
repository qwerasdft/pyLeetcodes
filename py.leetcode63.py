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
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        c=len(obstacleGrid[0])
        r=len(obstacleGrid)
        
        ans=[[0]*c for i in range(r)] 
        
        
        for i in range(r):
            for j in range(c):
                if i==0 :
                    ans[i][j]=1
                    if obstacleGrid[i][j]==1 :
                        ans[i][j]=0
                    if j>0 and ans[i][j-1]==0:
                        ans[i][j]=0
                
                elif j==0:
                    ans[i][j]=1
                    if obstacleGrid[i][j]==1 :
                        ans[i][j]=0
                    if i>0 and ans[i-1][j]==0:
                        ans[i][j]=0
                

                else :
                    if obstacleGrid[i][j]==1 :
                        ans[i][j]=0
                    else :
                        ans[i][j]  = ans[i-1][j]+ans[i][j-1]
                

        return ans[r-1][c-1]


if  __name__ == "__main__":
    a=[[0,0]]



    ret = Solution().uniquePathsWithObstacles(a)
    
    print(ret)
    

            