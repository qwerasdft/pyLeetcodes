class Solution:
    """
    Given an array of non-negative integers, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Your goal is to reach the last index in the minimum number of jumps.
    """
    # 結果超時

    def jump1(self, nums: "List[int]") -> int:
        ans = 99999

        def ansF(nums, index, jumpN, step):
            nonlocal ans
            if index == len(nums)-1:
                ans = min(ans, step)
                return ans

            for i in range(jumpN, 0, -1):
                if index+i < len(nums):
                    if not ans:
                        ansF(nums, index+i, nums[index+i], step+1)
                    else:
                        pass

        ansF(nums, 0, nums[0], 0)
        return ans

    def jump2(self, nums: "List[int]") -> int:
        n = len(nums)
        if len(nums) == 1:
            return 0
        ansT = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(nums[i]+1):
                try:
                    if i == 0:
                        ansT[i][i+j] = 1
                    else:
                        ansT[i][i+j] = 9999
                        for ii in range(i):
                            # 由上往下找最小的
                            if ansT[ii][i+j] != 0:
                                ansT[i][i+j] = min(ansT[i]
                                                   [i+j], ansT[ii][i+j]+1)
                        # 和左邊的比較看哪個路徑小
                        if ansT[i][i+j-1] != 0:
                            ansT[i][i+j] = min(ansT[i]
                                               [i+j], ansT[i][i+j-1])

                    # if i+j == n-1 and ansT[i][i+j] != 0:
                    #     # 如果最後一個就返回
                    #     return ansT[i][i+j]

                except:
                    pass
        for i in range(n):
            for j in range(n):
                print(ansT[i][j], end=" ")
            print()

    def jumpRes(self, nums):
        """
        這個問題有一個不錯的BFS結構。 讓我們使用問題語句中的示例
        nums = [2，3，1，1，4]進行說明。 我們最初位於位置0。
        然後我們最多可以從其移動nums [0]步。 因此，在一移動之後，我們可能會達到
        nums [1] = 3或nums [2] =1。因此，這些節點在一移動後即可到達。 從這些節點，
        我們可以進一步移動到nums [3] = 1和nums [4] =4。現在您可以看到目標nums [4] = 4
        可以在2步之內到達。 將它們放入代碼中，我們保留兩個指針start和end，
        它們記錄了起始節點的當前範圍。 每次執行移動操作後，將更新起始位置設置為end + 1，
        並將end設為從當前[start，end]開始執行1步操作可達到的最遠索引。 
        為了獲得可接受的解決方案，處理所有極端情況非常重要。 
        下面的代碼以統一的方式處理所有這些代碼，而不使用不干淨的if語句:-)
        """
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longestPos = 0
        curEnd = 0
        jumpN = 0

        for i in range(len(nums)-1):
            if i+nums[i] > longestPos:
                longestPos = i + nums[i]
            if i == curEnd:
                jumpN += 1
                curEnd = longestPos
        return jumpN


if __name__ == "__main__":
    a = [2, 3, 1, 1, 4]
    # a = [1]
    # a = [5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6,
    #      5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5]
    # a = [3, 2, 1, 0, 4]
    # a = [
    #     [5, 1, 9, 11],
    #     [2, 4, 8, 10],
    #     [13, 3, 6, 7],
    #     [15, 14, 12, 16]]

    print(Solution().jump(a))
