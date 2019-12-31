


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return None

        ans = self.stack.pop()

        return ans

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return min(self.stack)
        




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if  __name__ == "__main__":
    a=["push","push","push","getMin","pop","top","getMin"]
    b=[[-2],[0],[-3],[],[],[],[]]

    
    obj=MinStack()
    ans=[]
    for i,j in zip(a,b):
        if j:
            ans.append(obj.__getattribute__(i)(j[0]))
        else:
            ans.append(obj.__getattribute__(i)())

    print(ans)

