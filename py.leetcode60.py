# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# def listtolink(ls):
    
#     head=ListNode(0)
#     pre=head
    
#     for item in ls:
#         head.next=ListNode(item)
#         head=head.next
#     return pre.next

# def listNodeToString(node):
#     if not node:
#         return "[]"

#     result = ""
#     while node:
#         result += str(node.val) + ", "
#         node = node.next
#     return "[" + result[:-2] + "]"


import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        templist=[]
        temp=[i for i in range(1,n+1)]#定义一个n位的列表1-n

        dicts={1:1,2:1,3:2,4:6,5:24,6:120,7:720,8:5040,9:40320,10:362880}
        # 因为只要求1个，所以可以按照全排列的规则，一个个数的求出每个位置的数字，而不需要将所有的全排列字符串列出来。

        # 对于n个字符组成的字符串{1,2,3,...,n}，取第k个数时，首先可以求出第一个数，即(k-1)/(n-1个数的排列个数)。

        # 比如n=3，k=4时，全排列组合为：

        # 1 + {2,3}的全排列
        # 2 + {1,3}的全排列
        # 3 + {1,2}的全排列
    
        for i in range(n,0,-1):
            s = math.ceil(k / dicts[i])
            
            templist.append(temp.pop(s -1))
            k%=dicts[i]
        return ''.join([str(i) for i in templist])#将列表中数字先转化为str`


if  __name__ == "__main__":
    

    ret = Solution().getPermutation(7,123)
    
    print(ret)
    

            