class Solution:
    """
    Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

    The same repeated number may be chosen from candidates unlimited number of times.

    Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.
    """
    # 速度慢了第二種方法十倍

    def combinationSum(self, candidates: "List[int]", target: "int") -> "List[List[int]]":
        ans = []

        def ansF(candLi, num, tmpA):
            nonlocal ans
            if num == 0:
                ans.append(tmpA[:])
                return

            for i in candLi:
                if not tmpA and num-1 >= 0:
                    tmpA.append(i)
                    ansF(candLi, num-i, tmpA)
                    tmpA.pop()
                elif tmpA[-1] <= i and num-1 >= 0:
                    tmpA.append(i)
                    ansF(candLi, num-i, tmpA)
                    tmpA.pop()

        ansF(candidates, target, [])
        return ans
    # 這個方式的速度比較快

    def combinationSum1(self, candidates: "List[int]", target: "int") -> "List[List[int]]":
        ans = []

        def ansF(candLi, num, tmpA, index):
            nonlocal ans
            if num == 0:
                ans.append(tmpA[:])
                return

            for i in range(index, len(candLi)):
                if num-candLi[i] >= 0:
                    tmpA.append(candLi[i])
                    ansF(candLi, num-candLi[i], tmpA, i)
                    tmpA.pop()

        ansF(candidates, target, [], 0)
        return ans


if __name__ == "__main__":
    a = [2, 3, 5]
    t = 8
    a = [2, 3, 6, 7]
    t = 7
    # a = [2]
    # t = 1
    print(Solution().combinationSum(a, t))
