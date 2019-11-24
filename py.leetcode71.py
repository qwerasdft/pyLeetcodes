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



class Solution(object):
    def simplifyPath(self, path):
        a=path.split('/')
        ans=[]
        for i in a:
            if i=="" or i=='.':
                continue
            elif i=='..':
                try:
                    ans.pop()
                except:
                    pass
            else:
                ans.append(i)
        
        return '/'+'/'.join(ans)


if  __name__ == "__main__":
    a="/home//foo/"

    ret = Solution().simplifyPath(a)
    
    print(ret)
    

            