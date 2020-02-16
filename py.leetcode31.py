class Solution:
    """
    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

    If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

    The replacement must be in-place and use only constant extra memory.

    Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
    """

    def nextPermutation(self, nums: "List[int]") -> "None":
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                j = i

                # i之後排序
                # jEnd = len(nums)-1
                # while j < jEnd:
                #     k = j
                #     while k < jEnd:
                #         if nums[k] > nums[k+1]:
                #             nums[k], nums[k+1] = nums[k+1], nums[k]
                #         k += 1
                #     jEnd -= 1
                # j = i
                tmp = nums[i:]
                tmp.sort()
                nums[i:] = tmp[:]
                # 找到比i-1大的第一個數 然後置換
                while j < len(nums):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        return
                    j += 1

        nums[:] = nums[::-1]


if __name__ == "__main__":
    # a = [1, 3, 2]  # 213
    # a = [2, 3, 1]  # 312
    a = [5, 4, 7, 5, 3, 2]  # [5,5,2,3,4,7]
    # a = [3, 2, 1] # 123
    Solution().nextPermutation(a)
    print(a)
