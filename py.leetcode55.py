class Solution:
    """
    Given an array of non-negative integers, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Determine if you are able to reach the last index.
    """

    def canJump(self, nums: "List[int]") -> bool:
        nLen = len(nums)
        ans = nums[0]
        if nLen == 1:
            return True

        for i in range(1, nLen):
            ans -= 1
            if i == nLen-1 and ans >= 0:
                return True

            if ans < 0:
                return False

            ans = max(ans, nums[i])
            if i+ans >= nLen - 1:
                return True

        return False


if __name__ == "__main__":
    a = [2, 3, 1, 1, 4]
    # a = [2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8,
    #      0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6]
    # a = [1]
    # a = [3, 2, 1, 0, 4]
    a = [1, 2, 3]

    print(Solution().canJump(a))
