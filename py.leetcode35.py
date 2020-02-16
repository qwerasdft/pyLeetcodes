class Solution:
    """
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

    You are given a target value to search. If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.

    Your algorithm's runtime complexity must be in the order of O(log n).
    """

    def search(self, nums: "List[int]", target: "int") -> "int":
        ans = -1
        if len(nums) == 0:
            return ans

        def ansF(ini, end):
            nonlocal target, ans
            if ans != -1:
                return

            mid = ini+(ini-end)//2

            if (nums[mid] == target):
                ans = mid
                return
            elif nums[end] == target:
                ans = end
                return

            if ini >= end-1:
                return

            ansF(ini, mid-1)
            ansF(mid+1, end)

        ansF(0, len(nums)-1)
        return ans

    def search1(self, nums: "List[int]", target: "int") -> "int":
        ans = -1
        if len(nums) == 0:
            return ans

        def ansF(ini, end):
            nonlocal target, ans
            if ans != -1:
                return

            mid = ini+(end-ini)//2

            if (nums[mid] == target):
                ans = mid
                return
            elif nums[end] == target:
                ans = end
                return

            if ini >= end-1:
                return

            if nums[mid] >= nums[ini]:
                if target >= nums[ini] and target < nums[mid]:
                    ansF(ini, mid-1)
                else:
                    ansF(mid+1, end)
            else:
                if target > nums[mid] and target <= nums[end]:
                    ansF(mid+1, end)
                else:
                    ansF(ini, mid-1)
        ansF(0, len(nums)-1)
        return ans


if __name__ == "__main__":
    a = [4, 5, 6, 7, 0, 1, 2]
    a = [1, 3]
    print(Solution().search1(a, 3))
