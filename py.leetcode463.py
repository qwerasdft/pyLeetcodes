class Solution:
    """
    You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

    Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, 
    and there is exactly one island (i.e., one or more connected land cells).

    The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
    One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
    Determine the perimeter of the island.    """

    def islandPerimeter(self, grid: "List[List[int]]") -> "int":
        m = len(grid)
        n = len(grid[0])

        count = 0

        for m1 in range(m):
            for n1 in range(n):
                if grid[m1][n1] == 1:
                    edge = 0
                    if m1 > 0 and grid[m1-1][n1] == 1:
                        edge += 1

                    if m1 < m-1 and grid[m1+1][n1] == 1:
                        edge += 1

                    if n1 > 0 and grid[m1][n1-1] == 1:
                        edge += 1

                    if n1 < n-1 and grid[m1][n1+1] == 1:
                        edge += 1
                    count = count + 4-edge

        return count


if __name__ == "__main__":
    nums = [[0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]]

    print(Solution().islandPerimeter(nums))
