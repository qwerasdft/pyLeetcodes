import math


class Solution:
    """
    Given an integer, write a function to determine if it is a power of two.
    """

    def isPowerOfTwo(self, n: 'int') -> 'bool':
        if n <= 0:
            return False

        if math.log2(n).is_integer():
            return True
        return False


if __name__ == "__main__":
    a = 16

    print(Solution().isPowerOfTwo(a))
