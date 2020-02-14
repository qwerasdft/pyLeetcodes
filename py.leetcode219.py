class Solution:

    def containsNearbyDuplicate(self, nums: 'List[int]', k: 'int') -> 'bool':
        """
        Given an array of integers and an integer k, find out whether there are two distinct indices i 
        and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
        """
        window = set()
        for i in range(0, len(nums)):
            if len(window) >= k+1:
                window.remove(nums[i-k-1])
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False


if __name__ == "__main__":
    a = [1, 2, 3, 1]
    k = 3

    print(Solution().containsNearbyDuplicate(a, k))
