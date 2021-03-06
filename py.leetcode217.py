class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> 'bool':
        """
        Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
        """

        return True if len(set(nums)) != len(nums) else False


if __name__ == "__main__":
    a = [1, 2, 3, 1]

    print(Solution().containsDuplicate(a))
