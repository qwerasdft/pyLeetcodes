class Solution:
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    For example, given n = 3, a solution set is:

    [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
    ] 
    """

    def generateParenthesis(self, n: "int") -> "List[str]":
        ans = []

        def ansF(num, lnum, tmpS):
            nonlocal ans, n

            if num == n and len(tmpS) == n*2:
                ans.append(tmpS)
                return

            if num-1 >= 0 and lnum > 0:
                lnum -= 1
                ansF(num-1, lnum, tmpS+"(")
                lnum += 1
            if num + 1 <= n:
                ansF(num+1, lnum, tmpS+")")

        ansF(n, n, "")
        return ans


if __name__ == "__main__":
    a = 5

    print(Solution().generateParenthesis(a))
