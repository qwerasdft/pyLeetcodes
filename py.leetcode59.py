class Solution:
    """
    Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
    """

    def generateMatrix(self, n: "int") -> "List[List[int]]":
        u, d, l, r = 0, n-1, 0, n-1
        ind, maxN = 1, n*n
        ans = [[0 for i in range(n)] for j in range(n)]

        while u < d and l < r:
            for i in range(l, r):
                ans[u][i] = ind
                ind += 1
            for j in range(u, d):
                ans[j][r] = ind
                ind += 1
            for i in range(r, l, -1):
                ans[d][i] = ind
                ind += 1
            for j in range(d, u, -1):
                ans[j][l] = ind
                ind += 1
            u, d, l, r = u+1, d-1, l+1, r-1
        if l == r:
            for j in range(u, d+1):
                ans[j][l] = ind
                ind += 1
        elif u == d:
            for i in range(l, r+1):
                ans[u][i] = ind
                ind += 1
        return ans


if __name__ == "__main__":
    import pprint
    a = 4

    pprint.pprint(Solution().generateMatrix(a), width=20)
