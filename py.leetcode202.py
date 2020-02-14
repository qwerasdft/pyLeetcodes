class Solution:
    def isHappy(self, n):
        """
        Write an algorithm to determine if a number is "happy".

        A happy number is a number defined by the following process: 
        Starting with any positive integer, replace the number by the sum of 
        the squares of its digits, and repeat the process until the number 
        equals 1 (where it will stay), or it loops endlessly in a cycle which 
        does not include 1. Those numbers for which this process ends in 1 are happy
        """
        cycle = set()
        while n != 1 and n not in cycle:
            cycle.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n == 1


if __name__ == "__main__":
    a = 19

    print(Solution().isHappy(a))
