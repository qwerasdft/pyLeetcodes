class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        python中index、slice与slice assignment用法
        https://www.cnblogs.com/keviwu/p/5878180.html
        """
        
        
        if k > len(nums):
            k = k-len(nums)
        nums[:] = nums[-k: ] + nums[ :-k]


if  __name__ == "__main__":
    a=[1,2,3,4,5,6,7]
    Solution().rotate(a,3)

    print(a)

