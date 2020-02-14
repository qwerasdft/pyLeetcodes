

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > max:
                max = nums[i+1] - nums[i]
        return max


if __name__ == "__main__":
    a = [3, 6, 9, 1]

    print(Solution().maximumGap(a))
