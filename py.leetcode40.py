class Solution:
    """
    Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

    Each number in candidates may only be used once in the combination.

    Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.
    """

    def combinationSum2(self, candidates: "List[int]", target: "int") -> "List[List[int]]":
        ans = []
        candidates.sort()

        def ansF(candLi, num, tmpA):
            nonlocal ans
            if num == 0:
                ans.append(tmpA)
                return

            for i in range(len(candLi)):
                if i-1 >= 0 and candLi[i] == candLi[i-1]:
                    continue
                if num-candLi[i] >= 0:

                    ansF(candLi[i+1:], num-candLi[i], tmpA+[candLi[i]])

        ansF(candidates, target, [])
        return ans


if __name__ == "__main__":
    # a = [2, 3, 5]
    # t = 8
    a = [10, 1, 2, 7, 6, 1, 5]
    t = 8
    # a = [1]
    # t = 1
    print(Solution().combinationSum2(a, t))
