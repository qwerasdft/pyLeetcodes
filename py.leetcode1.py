class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic1 = {}

        for a in range(len(nums)):
            gap = target - nums[a]

            if gap in dic1:
                return [dic1[gap], a]

            dic1[nums[a]] = a


if __name__ == "__main__":
    a = [2, 7, 11, 15]
    b = 9
    # test = Solution()
    print(Solution().twoSum(a, b))
