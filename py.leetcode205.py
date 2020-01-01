class Solution:
    def isIsomorphic(self, s: 'str', t: 'str') -> 'bool':
        """
        Given two strings s and t, determine if they are isomorphic.

        Two strings are isomorphic if the characters in s can be replaced to get t.

        All occurrences of a character must be replaced with another character while 
        preserving the order of characters. No two characters may map to the same character 
        but a character may map to itself.
        """
        
        an1=''
        an2=''
        ch={}
        ch2={}
        
        i=0
        for w in s:
            if w not in ch:
                ch[w]=str(i)
                an1+=str(i)
                i+=1
            else:
                an1+=ch[w]
        
        i=0
        for w in t:
            if w not in ch2:
                ch2[w]=str(i)
                an2+=str(i)
                i+=1
            else:
                an2+=ch2[w]
        
        return an1==an2 
        

if  __name__ == "__main__":
    s="egg"
    t="add"
    

    print(Solution().isIsomorphic(s,t))

