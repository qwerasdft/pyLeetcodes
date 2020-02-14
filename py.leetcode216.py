class Solution:
    def combinationSum3(self, k: 'int', n: 'int') -> 'List[List[int]]':
        """
        Find all possible combinations of k numbers that add up to a number n, 
        given that only numbers from 1 to 9 can be used and each combination 
        should be a unique set of numbers.
        """

        seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        ans = []

        def fun(k, n, tmp, ind):
            nonlocal seq

            if n == 0 and k == 0:

                ans.append(tmp)
                return

            if ind == 9 or n < 0 or k < 0:
                return

            for i in range(ind, 9):

                fun(k-1, n-seq[i], tmp+[seq[i]], i+1)

        fun(k, n, [], 0)
        return ans


if __name__ == "__main__":
    k = 3
    n = 9

    print(Solution().combinationSum3(k, n))
