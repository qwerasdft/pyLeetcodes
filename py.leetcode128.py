
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# def stringToTreeNode(input):
#     input = input.strip()
#     input = input[1:-1]
#     if not input:
#         return None

#     inputValues = [s.strip() for s in input.split(',')]
#     root = TreeNode(int(inputValues[0]))
#     nodeQueue = [root]
#     front = 0
#     index = 1
#     while index < len(inputValues):
#         node = nodeQueue[front]
#         front = front + 1

#         item = inputValues[index]
#         index = index + 1
#         if item != "null":
#             leftNumber = int(item)
#             node.left = TreeNode(leftNumber)
#             nodeQueue.append(node.left)

#         if index >= len(inputValues):
#             break

#         item = inputValues[index]
#         index = index + 1
#         if item != "null":
#             rightNumber = int(item)
#             node.right = TreeNode(rightNumber)
#             nodeQueue.append(node.right)
#     return root
    
class Solution:
    def longestConsecutive(self, nums: "List[int]") -> int:
        numset=set(nums)
        
        long=0
        for num in nums:
            """
            #如果num-1存在,表示這num不是連續數字的開頭
            #這樣我們就跳過這個數字
            """
            if num-1 in numset:
                continue
            
            count=0
            while num in numset:
                
                count+=1
                num+=1
            
            long=long if long>count else count
        
        return long
        
if  __name__ == "__main__":
    a=[100,4,200,1,3,2]
   

    ret = Solution().longestConsecutive(a)
    
    print(ret)
