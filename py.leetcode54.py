class Solution:
    """
    Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

    """

    def spiralOrder(self, matrix: "List[List[int]]") -> "List[int]":
        ans = []

        try:
            m = len(matrix)
            n = len(matrix[0])
        except:
            return matrix

        u, d, l, r = 0, m-1, 0, n-1
        while u < d and l < r:
            ans.extend([matrix[u][i] for i in range(l, r)])
            ans.extend([matrix[i][r] for i in range(u, d)])
            ans.extend([matrix[d][i] for i in range(r, l, -1)])
            ans.extend([matrix[i][l] for i in range(d, u, -1)])
            u, d, l, r = u+1, d-1, l+1, r-1
        if l == r:
            ans.extend([matrix[i][r] for i in range(u, d + 1)])
        elif u == d:
            ans.extend([matrix[d][i] for i in range(l, r + 1)])

        return ans


if __name__ == "__main__":
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    a = [[1], [2]]

    print(Solution().spiralOrder(a))
