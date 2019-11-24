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
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        h=len(board)
        w=len(board[0])
        
        def check(x,y,board,word,wind):
            ans = False

            tmpw=""
            tmpw,board[y][x]=board[y][x],tmpw

            if wind == len(word)-1:
                return True

            if y>0 and board[y-1][x]==word[wind+1]:
                ans = ans or check(x,y-1,board,word,wind+1)
            if y<h-1 and board[y+1][x]==word[wind+1]:
                ans = ans or check(x,y+1,board,word,wind+1)
            if x>0 and board[y][x-1]==word[wind+1]:
                ans = ans or check(x-1,y,board,word,wind+1)
            if x<w-1 and board[y][x+1]==word[wind+1]:
                ans = ans or check(x+1,y,board,word,wind+1)
            
            tmpw,board[y][x]=board[y][x],tmpw

            return ans


        
        ans = False
        for i in range(h):
            for j in range(w):
                if board[i][j]==word[0]:
                    ans = ans or check(j,i,board,word,0)
        
        return ans



    
if  __name__ == "__main__":
    a=[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']]
    b="ABFCs"

    a1=[["a","a"]]
    b1="aaa"

    ret = Solution().exist(a1,b1)
    
    print(ret)
