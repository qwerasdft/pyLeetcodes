# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# def listtolk(ls):
    
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
    def myAtoi(self, str1: 'str') -> 'int':
        
        ans=''
        if str1=='':
            return 0
        
        for i in range(len(str1)):
            if str1[i] ==" ":
                continue
            else:
                str1=str1[i:]
                break
        
        tmp=''
        for w in str1:            
            
            if not w.isdigit():
                if w=='-' or w=="+":
                    if tmp != '':
                        break
                    elif ans !="":
                        break
                    tmp=w
                    
                else:
                    break
                       
            
            else:
                if tmp=='-' and ans=='':
                    ans=ans+tmp+w
                    tmp==''
                else:
                    ans+=w
                    
        if ans=='':
            return 0
        ans = int(''.join(ans))
        if ans >= 2147483647:
            return 2147483647
        elif ans <= -2147483648:
            return -2147483648
        else:
            return ans
        
        
if  __name__ == "__main__":
    a="123453"

    ret = Solution().myAtoi(a)
    
    print(ret)

            