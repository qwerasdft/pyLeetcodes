class Solution:
    """
    Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
    connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are 
    surrounded by water.

    Find the maximum area of an island in the given 2D array. 
    (If there is no island, the maximum area is 0.) 
    """

    def maxAreaOfIsland(self, grid: "List[List[int]]") -> "int":

        n = len(grid)
        m = len(grid[0])

        def check(r, c, num):
            nonlocal n, m
            num += 1
            grid[r][c] = 2
            if r > 0 and grid[r-1][c] == 1:
                num = max(num, check(r-1, c, num))

            if c > 0 and grid[r][c-1] == 1:
                num = max(num, check(r, c-1, num))

            if r < n-1 and grid[r+1][c] == 1:
                num = max(num, check(r+1, c, num))
            if c < m-1 and grid[r][c+1] == 1:
                num = max(num, check(r, c+1, num))
            return num
        ans = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    ans = max(ans, check(r, c, 0))
        return ans


if __name__ == "__main__":
    islands = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
               [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    print(Solution().maxAreaOfIsland(islands))
