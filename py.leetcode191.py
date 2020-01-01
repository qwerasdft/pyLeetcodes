class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        b=0
        while n >0:
            if n %2:
                b+=1

            n= (n-(n%2))/2
        return b

if  __name__ == "__main__":
    a=int('00000000000000000000000000001011',2)
    

    print(Solution().hammingWeight(a))

