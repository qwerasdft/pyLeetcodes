class Solution:
    """
    You are given an n x n 2D matrix representing an image.

    Rotate the image by 90 degrees (clockwise).

    Note:

    You have to rotate the image in-place, which means you have to modify the
    input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
    """

    def rotate(self, A):
        n = len(A)
        # 對角線翻轉
        for i in range(n):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        # 左右翻轉
        for row in A:
            for j in range(n//2):
                row[j], row[~j] = row[~j], row[j]


if __name__ == "__main__":
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    # a = [
    #     [5, 1, 9, 11],
    #     [2, 4, 8, 10],
    #     [13, 3, 6, 7],
    #     [15, 14, 12, 16]]
    Solution().rotate(a)
    print(a)
