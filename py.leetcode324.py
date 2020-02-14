class Solution:
    """
    Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
    """

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        arr = sorted(nums)
        for i in range(1, len(nums), 2):
            nums[i] = arr.pop()
        for i in range(0, len(nums), 2):
            nums[i] = arr.pop()


if __name__ == "__main__":
    nums = [1, 5, 1, 1, 6, 4]
    Solution().wiggleSort(nums)
    print(nums)
