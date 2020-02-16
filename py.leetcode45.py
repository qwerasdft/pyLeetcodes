class Solution:
    """
    Given an array of non-negative integers, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Your goal is to reach the last index in the minimum number of jumps.
    """

    def jump(self, nums: "List[int]") -> int:
        ans = float("+inf")

        def ansF(nums, index, jumpN, step):
            nonlocal ans
            if index == len(nums)-1:
                ans = min(ans, step)
                return

            for i in range(jumpN, 0, -1):
                if index+i < len(nums):
                    ansF(nums, index+i, nums[index+i], step+1)

        ansF(nums, 0, nums[0], 0)
        return ans


if __name__ == "__main__":
    a = [2, 3, 1, 1, 4]
    a = [5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6,
         5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5]
    # a = [3, 2, 1, 0, 4]
    # a = [
    #     [5, 1, 9, 11],
    #     [2, 4, 8, 10],
    #     [13, 3, 6, 7],
    #     [15, 14, 12, 16]]

    print(Solution().jump(a))
