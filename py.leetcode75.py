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

class Solution:
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1
        
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1                    
        #     tmp.append(nums[:])
        # for _ in tmp:
        #     print(_)
                    
                
    
# 608/5000
# 這是荷蘭的分區問題。 我們將數組分為四類：紅色，白色，未分類和藍色。 
# 最初，我們將所有元素歸為未分類。 只要白色指針小於藍色指針，我們就會
# 從頭開始進行迭代。 如果白色指針是紅色的（nums [white] == 0），我們
# 將與紅色指針交換並將白色和紅色指針向前移動。 如果指針為白色（nums [
# white] == 1），則該元素已經在正確的位置，因此我們不必交換，只需向前
# 移動白色指針即可。 如果白色指針為藍色，我們將交換最新的未分類元素。        
            
        

if  __name__ == "__main__":
    a=[2,0,2,1,1,0]
    Solution().sortColors(a)
    
    print(a)
