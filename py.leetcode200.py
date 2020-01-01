class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid ==[]:
            return 0
        
        r= len(grid)
        c= len(grid[0])
        count = 0

        def helper(i,j):
            if i>=0 and i < r and j >=0 and j < c and grid[i][j]== '1':
                grid[i][j]='#'
                helper(i+1,j)
                helper(i-1,j)
                helper(i,j+1)
                helper(i,j-1)
            else:
                return
        
        
        for i in range(r):
            for j in range(c):
                #print(i,j,grid[i][j])
                if grid[i][j] == '1':
                    
                    helper(i,j)
                    
                    count +=1
                    
        return count
        

if  __name__ == "__main__":
    a=[["1","1","1","1","0"],
       ["1","1","0","1","0"],
       ["1","1","0","0","0"],
       ["0","0","0","0","0"]]
    

    print(Solution().numIslands(a))

