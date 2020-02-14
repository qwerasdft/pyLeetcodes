class Solution:
    """
    Write an efficient algorithm that searches for a value in an m x n matrix. 
                                            This matrix has the following properties:
    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
    """

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = len(matrix)
        for i in range(r):
            if target in matrix[i]:
                return True
        return False


if __name__ == "__main__":
    a = [[1,   4,  7, 11, 15],
         [2,   5,  8, 12, 19],
         [3,   6,  9, 16, 22],
         [10, 13, 14, 17, 24],
         [18, 21, 23, 26, 30]
         ]
    t = 5

    print(Solution().searchMatrix(a, t))
