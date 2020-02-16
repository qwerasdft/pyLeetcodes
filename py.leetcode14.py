class Solution:
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "". 
    """

    def longestCommonPrefix(self, strs: "List[str]") -> "str":
        if len(strs) == 0:
            return ""

        tmpStr = strs[0]

        while 1:
            if (all(s.startswith(tmpStr) for s in strs)):
                return tmpStr
            tmpStr = tmpStr[:-1]


if __name__ == "__main__":
    a = ["flower", "flow", "flight"]

    print(Solution().longestCommonPrefix(a))
