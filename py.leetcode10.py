class Solution:
    """
    Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.
    """

    def isMatch(self, s: str, p: str) -> bool:
        pLen = len(p)
        sLen = len(s)

        dp = [[0 for _ in range(pLen+1)] for _ in range(sLen+1)]
        dp[0][0] = 1
        """
        /* based case */
        /* initialize first row of pattern when s is empty, because even s is empty,
        /* there still be cases that two string matching such as : s="", p= a*b* */ 
        """
        for i in range(1, pLen+1):
            if p[i-1] == "*" and dp[0][i-2]:
                dp[0][i] = 1

        for i in range(1, sLen+1):
            for j in range(1, pLen+1):
                if s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                #  if char at i,j are the same, matching status depends on previous i-1, j-1 status
                elif p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                # '.' mactches everything, dont need to consider cur char at index i
                elif p[j-1] == "*":
                    # If the character before the star matches char in the string,
                    # the star can match 0 of the char before it, or at least 1.
                    # match[i][j-2] is for matching 0, cause we need to skip the last 2
                    # characters in the pattern. match[i - 1][j] is for matching 1, cause
                    # we need to skip 1 character in the string, but keep the entire pattern
                    if p[j-2] == s[i-1] or p[j-2] == ".":
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    # If the character before the star does not match the char in the string,
                    # then the only way to get a match is if the star matches 0 characters
                    else:
                        dp[i][j] = dp[i][j-2]
        return dp[sLen][pLen]


if __name__ == "__main__":
    s = "aa"
    p = "a*"
    # p = "mis*is*ip*."
    # s = "aa"
    # p = "a*"
    print(Solution().isMatch(s, p))
